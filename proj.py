import os
import requests

def run_graphql_query(query, token, variables=None):
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"query": query, "variables": variables}
    response = requests.post("https://api.github.com/graphql", json=payload, headers=headers)
    response.raise_for_status()
    return response.json()

def get_classic_projects(token, owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/projects"
    headers = {
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_v2_projects(token, owner, repo):
    query = """
    query ($owner: String!, $repo: String!) {
        repository(owner: $owner, name: $repo) {
            owner {
                __typename
                ... on Organization {
                    projectsV2(first: 100) {
                        nodes {
                            id
                            title
                            repositories(first: 100) {
                                nodes { name }
                            }
                        }
                    }
                }
                ... on User {
                    projectsV2(first: 100) {
                        nodes {
                            id
                            title
                            repositories(first: 100) {
                                nodes { name }
                            }
                        }
                    }
                }
            }
        }
    }
    """
    variables = {"owner": owner, "repo": repo}
    result = run_graphql_query(query, token, variables)
    owner_data = result["data"]["repository"]["owner"]
    
    # Extract projects based on owner type (Organization/User)
    projects_raw = []
    if owner_data["__typename"] == "Organization":
        projects_raw = owner_data.get("projectsV2", {}).get("nodes", [])
    elif owner_data["__typename"] == "User":
        projects_raw = owner_data.get("projectsV2", {}).get("nodes", [])
    
    # Filter projects linked to the target repository
    v2_projects = []
    for project in projects_raw:
        repo_nodes = project.get("repositories", {}).get("nodes", [])
        if any(r["name"] == repo for r in repo_nodes):
            v2_projects.append({
                "id": project["id"],
                "title": project["title"],
                "url": f"https://github.com/orgs/{owner}/projects/{project['number']}"
            })
    return v2_projects

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo_full_name = os.getenv("GITHUB_REPOSITORY")
    owner, repo = repo_full_name.split("/")
    
    classic_projects = get_classic_projects(token, owner, repo)
    v2_projects = get_v2_projects(token, owner, repo)
    
    print("Classic Projects:", [p["name"] for p in classic_projects])
    print("V2 Projects:", [p["title"] for p in v2_projects])

if __name__ == "__main__":
    main()
