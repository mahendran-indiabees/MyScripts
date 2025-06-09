#!/usr/bin/env python3
"""
GitHub Projects Lister

A Python script to list GitHub Classic and New projects using GraphQL and REST APIs.
Supports both repository-level and organization-level projects.
"""

import argparse
import json
import logging
import os
import sys
from typing import Dict, List, Optional, Union
import requests


class GitHubProjectsLister:
    """Main class for listing GitHub projects using REST and GraphQL APIs."""
    
    def __init__(self, token: str, verbose: bool = False):
        """
        Initialize the GitHub Projects Lister.
        
        Args:
            token: GitHub personal access token
            verbose: Enable verbose logging
        """
        self.token = token
        self.headers = {
            'Authorization': f'token {token}',
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'GitHub-Projects-Lister/1.0'
        }
        self.graphql_headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-Agent': 'GitHub-Projects-Lister/1.0'
        }
        
        # Setup logging
        log_level = logging.DEBUG if verbose else logging.INFO
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
        
        # API endpoints
        self.rest_base_url = 'https://api.github.com'
        self.graphql_url = 'https://api.github.com/graphql'

    def make_rest_request(self, url: str, params: Optional[Dict] = None) -> Dict:
        """
        Make a REST API request with error handling and rate limit management.
        
        Args:
            url: API endpoint URL
            params: Query parameters
            
        Returns:
            JSON response data
            
        Raises:
            Exception: If request fails or rate limit exceeded
        """
        try:
            response = requests.get(url, headers=self.headers, params=params)
            
            # Check rate limit
            remaining = int(response.headers.get('X-RateLimit-Remaining', 0))
            if remaining < 10:
                self.logger.warning(f"Rate limit low: {remaining} requests remaining")
            
            if response.status_code == 403 and 'rate limit' in response.text.lower():
                reset_time = response.headers.get('X-RateLimit-Reset')
                raise Exception(f"Rate limit exceeded. Resets at: {reset_time}")
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"REST API request failed: {e}")
            raise Exception(f"Failed to make REST request to {url}: {e}")

    def make_graphql_request(self, query: str, variables: Optional[Dict] = None) -> Dict:
        """
        Make a GraphQL request with error handling.
        
        Args:
            query: GraphQL query string
            variables: Query variables
            
        Returns:
            GraphQL response data
            
        Raises:
            Exception: If request fails or contains errors
        """
        try:
            payload = {'query': query}
            if variables:
                payload['variables'] = variables
                
            response = requests.post(
                self.graphql_url,
                headers=self.graphql_headers,
                json=payload
            )
            
            response.raise_for_status()
            data = response.json()
            
            if 'errors' in data:
                error_msg = '; '.join([error['message'] for error in data['errors']])
                raise Exception(f"GraphQL errors: {error_msg}")
                
            return data
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"GraphQL request failed: {e}")
            raise Exception(f"Failed to make GraphQL request: {e}")

    def get_repository_info(self, owner: str, repo: str) -> Dict:
        """
        Get repository information including node ID for GraphQL queries.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            Repository information
        """
        url = f"{self.rest_base_url}/repos/{owner}/{repo}"
        self.logger.debug(f"Fetching repository info: {owner}/{repo}")
        return self.make_rest_request(url)

    def list_classic_projects_rest(self, owner: str, repo: str) -> List[Dict]:
        """
        List Classic Projects (V1) using REST API.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            List of classic projects
        """
        self.logger.info("Fetching Classic Projects using REST API...")
        
        projects = []
        page = 1
        per_page = 100
        
        while True:
            url = f"{self.rest_base_url}/repos/{owner}/{repo}/projects"
            params = {
                'state': 'all',
                'page': page,
                'per_page': per_page
            }
            
            # Need to use projects preview header for classic projects
            headers = self.headers.copy()
            headers['Accept'] = 'application/vnd.github.inertia-preview+json'
            
            try:
                response = requests.get(url, headers=headers, params=params)
                response.raise_for_status()
                page_projects = response.json()
                
                if not page_projects:
                    break
                    
                projects.extend(page_projects)
                
                if len(page_projects) < per_page:
                    break
                    
                page += 1
                
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Failed to fetch classic projects: {e}")
                break
        
        self.logger.info(f"Found {len(projects)} Classic Projects")
        return projects

    def list_organization_classic_projects_rest(self, org: str) -> List[Dict]:
        """
        List organization-level Classic Projects using REST API.
        
        Args:
            org: Organization name
            
        Returns:
            List of organization classic projects
        """
        self.logger.info(f"Fetching Organization Classic Projects for {org}...")
        
        projects = []
        page = 1
        per_page = 100
        
        while True:
            url = f"{self.rest_base_url}/orgs/{org}/projects"
            params = {
                'state': 'all',
                'page': page,
                'per_page': per_page
            }
            
            headers = self.headers.copy()
            headers['Accept'] = 'application/vnd.github.inertia-preview+json'
            
            try:
                response = requests.get(url, headers=headers, params=params)
                response.raise_for_status()
                page_projects = response.json()
                
                if not page_projects:
                    break
                    
                projects.extend(page_projects)
                
                if len(page_projects) < per_page:
                    break
                    
                page += 1
                
            except requests.exceptions.RequestException as e:
                self.logger.error(f"Failed to fetch org classic projects: {e}")
                break
        
        self.logger.info(f"Found {len(projects)} Organization Classic Projects")
        return projects

    def list_new_projects_graphql(self, owner: str, repo: str) -> List[Dict]:
        """
        List New Projects (V2) using GraphQL API.
        
        Args:
            owner: Repository owner
            repo: Repository name
            
        Returns:
            List of new projects
        """
        self.logger.info("Fetching New Projects (V2) using GraphQL...")
        
        query = """
        query($owner: String!, $repo: String!, $cursor: String) {
          repository(owner: $owner, name: $repo) {
            projectsV2(first: 100, after: $cursor) {
              totalCount
              pageInfo {
                hasNextPage
                endCursor
              }
              nodes {
                id
                number
                title
                shortDescription
                readme
                closed
                closedAt
                createdAt
                updatedAt
                url
                creator {
                  login
                }
                owner {
                  ... on User {
                    login
                  }
                  ... on Organization {
                    login
                  }
                }
              }
            }
          }
        }
        """
        
        projects = []
        cursor = None
        
        while True:
            variables = {
                'owner': owner,
                'repo': repo,
                'cursor': cursor
            }
            
            try:
                data = self.make_graphql_request(query, variables)
                
                if not data.get('data', {}).get('repository'):
                    self.logger.warning("Repository not found or no access")
                    break
                
                projects_data = data['data']['repository']['projectsV2']
                projects.extend(projects_data['nodes'])
                
                if not projects_data['pageInfo']['hasNextPage']:
                    break
                    
                cursor = projects_data['pageInfo']['endCursor']
                
            except Exception as e:
                self.logger.error(f"Failed to fetch new projects: {e}")
                break
        
        self.logger.info(f"Found {len(projects)} New Projects (V2)")
        return projects

    def list_organization_new_projects_graphql(self, org: str) -> List[Dict]:
        """
        List organization-level New Projects (V2) using GraphQL.
        
        Args:
            org: Organization name
            
        Returns:
            List of organization new projects
        """
        self.logger.info(f"Fetching Organization New Projects (V2) for {org}...")
        
        query = """
        query($org: String!, $cursor: String) {
          organization(login: $org) {
            projectsV2(first: 100, after: $cursor) {
              totalCount
              pageInfo {
                hasNextPage
                endCursor
              }
              nodes {
                id
                number
                title
                shortDescription
                readme
                closed
                closedAt
                createdAt
                updatedAt
                url
                creator {
                  login
                }
                owner {
                  ... on User {
                    login
                  }
                  ... on Organization {
                    login
                  }
                }
              }
            }
          }
        }
        """
        
        projects = []
        cursor = None
        
        while True:
            variables = {
                'org': org,
                'cursor': cursor
            }
            
            try:
                data = self.make_graphql_request(query, variables)
                
                if not data.get('data', {}).get('organization'):
                    self.logger.warning("Organization not found or no access")
                    break
                
                projects_data = data['data']['organization']['projectsV2']
                projects.extend(projects_data['nodes'])
                
                if not projects_data['pageInfo']['hasNextPage']:
                    break
                    
                cursor = projects_data['pageInfo']['endCursor']
                
            except Exception as e:
                self.logger.error(f"Failed to fetch org new projects: {e}")
                break
        
        self.logger.info(f"Found {len(projects)} Organization New Projects (V2)")
        return projects

    def format_classic_project(self, project: Dict) -> Dict:
        """Format classic project data for display."""
        return {
            'type': 'Classic Project (V1)',
            'id': project.get('id'),
            'number': project.get('number'),
            'name': project.get('name'),
            'body': project.get('body', '').strip()[:100] + '...' if project.get('body', '').strip() else 'No description',
            'state': project.get('state'),
            'url': project.get('html_url'),
            'created_at': project.get('created_at'),
            'updated_at': project.get('updated_at'),
            'creator': project.get('creator', {}).get('login') if project.get('creator') else 'Unknown'
        }

    def format_new_project(self, project: Dict) -> Dict:
        """Format new project data for display."""
        return {
            'type': 'New Project (V2)',
            'id': project.get('id'),
            'number': project.get('number'),
            'name': project.get('title'),
            'body': project.get('shortDescription', '').strip()[:100] + '...' if project.get('shortDescription', '').strip() else 'No description',
            'state': 'closed' if project.get('closed') else 'open',
            'url': project.get('url'),
            'created_at': project.get('createdAt'),
            'updated_at': project.get('updatedAt'),
            'creator': project.get('creator', {}).get('login') if project.get('creator') else 'Unknown',
            'closed_at': project.get('closedAt')
        }

    def print_projects_summary(self, all_projects: List[Dict]):
        """Print a formatted summary of all projects."""
        if not all_projects:
            print("\n🔍 No projects found for this repository.")
            return
        
        print(f"\n📊 Found {len(all_projects)} total projects\n")
        print("=" * 100)
        
        for i, project in enumerate(all_projects, 1):
            print(f"\n{i}. {project['type']}")
            print(f"   📋 Name: {project['name']}")
            print(f"   🆔 ID: {project['id']}")
            print(f"   🔢 Number: #{project['number']}")
            print(f"   📝 Description: {project['body']}")
            print(f"   🏷️  State: {project['state']}")
            print(f"   👤 Creator: {project['creator']}")
            print(f"   🔗 URL: {project['url']}")
            print(f"   📅 Created: {project['created_at']}")
            print(f"   🔄 Updated: {project['updated_at']}")
            if project.get('closed_at'):
                print(f"   🔒 Closed: {project['closed_at']}")
            print("-" * 80)

    def export_to_json(self, projects: List[Dict], filename: str):
        """Export projects data to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(projects, f, indent=2, default=str)
            print(f"\n💾 Projects data exported to: {filename}")
        except Exception as e:
            self.logger.error(f"Failed to export to JSON: {e}")

    def run(self, owner: str, repo: str, include_org: bool = False, 
            export_json: str = None) -> List[Dict]:
        """
        Main method to run the project listing.
        
        Args:
            owner: Repository owner
            repo: Repository name
            include_org: Include organization-level projects
            export_json: Export results to JSON file
            
        Returns:
            List of all projects found
        """
        print(f"🚀 Listing GitHub Projects for {owner}/{repo}")
        print("=" * 60)
        
        all_projects = []
        
        try:
            # Verify repository exists
            repo_info = self.get_repository_info(owner, repo)
            print(f"📁 Repository: {repo_info['full_name']}")
            print(f"🔗 URL: {repo_info['html_url']}")
            
            # Get Classic Projects (V1) using REST
            try:
                classic_projects = self.list_classic_projects_rest(owner, repo)
                formatted_classic = [self.format_classic_project(p) for p in classic_projects]
                all_projects.extend(formatted_classic)
            except Exception as e:
                self.logger.error(f"Failed to fetch classic projects: {e}")
            
            # Get New Projects (V2) using GraphQL
            try:
                new_projects = self.list_new_projects_graphql(owner, repo)
                formatted_new = [self.format_new_project(p) for p in new_projects]
                all_projects.extend(formatted_new)
            except Exception as e:
                self.logger.error(f"Failed to fetch new projects: {e}")
            
            # Get organization-level projects if requested
            if include_org:
                try:
                    org_classic = self.list_organization_classic_projects_rest(owner)
                    formatted_org_classic = [self.format_classic_project(p) for p in org_classic]
                    all_projects.extend(formatted_org_classic)
                    
                    org_new = self.list_organization_new_projects_graphql(owner)
                    formatted_org_new = [self.format_new_project(p) for p in org_new]
                    all_projects.extend(formatted_org_new)
                except Exception as e:
                    self.logger.error(f"Failed to fetch organization projects: {e}")
            
            # Print summary
            self.print_projects_summary(all_projects)
            
            # Export to JSON if requested
            if export_json:
                self.export_to_json(all_projects, export_json)
            
            return all_projects
            
        except Exception as e:
            self.logger.error(f"Failed to run project listing: {e}")
            sys.exit(1)


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='List GitHub Classic and New projects using REST and GraphQL APIs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python github_projects_lister.py octocat Hello-World
  python github_projects_lister.py microsoft vscode --include-org --verbose
  python github_projects_lister.py facebook react --export projects.json
  
Environment Variables:
  GITHUB_TOKEN - GitHub personal access token (required)
        """
    )
    
    parser.add_argument('owner', help='Repository owner (username or organization)')
    parser.add_argument('repo', help='Repository name')
    parser.add_argument('--include-org', action='store_true',
                       help='Include organization-level projects')
    parser.add_argument('--export', metavar='FILE',
                       help='Export results to JSON file')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    parser.add_argument('--token', 
                       help='GitHub personal access token (or use GITHUB_TOKEN env var)')
    
    args = parser.parse_args()
    
    # Get GitHub token
    token = args.token or os.getenv('GITHUB_TOKEN')
    if not token:
        print("❌ Error: GitHub token is required!")
        print("Set GITHUB_TOKEN environment variable or use --token argument")
        print("\nTo create a token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Generate a new token with 'repo' and 'project' scopes")
        print("3. For organization projects, ensure the token has appropriate org permissions")
        sys.exit(1)
    
    # Create lister instance and run
    try:
        lister = GitHubProjectsLister(token, verbose=args.verbose)
        projects = lister.run(
            owner=args.owner,
            repo=args.repo,
            include_org=args.include_org,
            export_json=args.export
        )
        
        print(f"\n✅ Successfully listed {len(projects)} projects!")
        
    except KeyboardInterrupt:
        print("\n🛑 Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
