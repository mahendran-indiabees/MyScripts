import os
import requests
import json

def run_graphql_query(query, token, variables=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {'query': query}
    if variables:
        payload['variables'] = variables
        
    response = requests.post(
        'https://api.github.com/graphql',
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    return response.json()

def get_classic_projects(token, owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/projects"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_v2_projects(token, owner, repo):
    query = """
    query($owner: String!, $repo: String!) {
        repository(owner: $owner, name: $repo) {
            projectsV2(first: 100) {
                nodes {
                    id
                    number
                    title
                    url
                    shortDescription
                }
            }
        }
    }
    """
    variables = {"owner": owner, "repo": repo}
    result = run_graphql_query(query, token, variables)
    return result['data']['repository']['projectsV2']['nodes']

def main():
    token = os.getenv('GITHUB_TOKEN')
    repo_full_name = os.getenv('GITHUB_REPOSITORY')
    
    if not token or not repo_full_name:
        raise ValueError("Missing environment variables")
    
    owner, repo = repo_full_name.split('/')
    
    print("Fetching projects...")
    
    # Get classic projects
    classic_projects = get_classic_projects(token, owner, repo)
    
    # Get V2 projects
    v2_projects = get_v2_projects(token, owner, repo)
    
    # Print results
    print("\nClassic Projects:")
    for project in classic_projects:
        print(f"- {project['name']} (ID: {project['id']}, URL: {project['html_url']})")
    
    print("\nV2 Projects:")
    for project in v2_projects:
        print(f"- {project['title']} (Number: {project['number']}, URL: {project['url']})")
    
    # Create step summary in GitHub Actions
    if os.getenv('GITHUB_STEP_SUMMARY'):
        with open(os.getenv('GITHUB_STEP_SUMMARY'), 'a') as f:
            f.write("## GitHub Projects Report\n")
            f.write("### Classic Projects\n")
            for project in classic_projects:
                f.write(f"- [{project['name']}]({project['html_url']}) (ID: `{project['id']}`)\n")
            
            f.write("\n### New Projects (V2)\n")
            for project in v2_projects:
                f.write(f"- [{project['title']}]({project['url']}) (Number: `{project['number']}`)\n")

if __name__ == "__main__":
    main()
