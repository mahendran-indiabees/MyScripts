import requests
import os

# Configuration - Replace with your details
REPO_OWNER = "your_github_username"
REPO_NAME = "your_repository_name"
GITHUB_TOKEN = os.getenv("GITHUB_PAT")  # Store token in environment variable

# GraphQL API Endpoint
GRAPHQL_URL = "https://api.github.com/graphql"

def get_github_projects():
    """Fetch both new (ProjectV2) and classic projects for a repository"""
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28"  # Latest REST API version :cite[7]
    }
    
    # GraphQL query to fetch both project types
    query = f"""
    query {{
      repository(owner: "{REPO_OWNER}", name: "{REPO_NAME}") {{
        # Fetch new projects (ProjectV2)
        projectsV2(first: 100) {{
          nodes {{
            title
            number
          }}
        }}
        # Fetch classic projects
        projects(first: 100, states: OPEN) {{
          nodes {{
            name
            number
          }}
        }}
      }}
    }}
    """
    
    try:
        response = requests.post(
            url=GRAPHQL_URL,
            json={"query": query},
            headers=headers
        )
        response.raise_for_status()
        data = response.json()
        
        return data["data"]["repository"]
    
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {str(e)}")
        return None

def print_project_details(projects_data):
    """Print project details with classification"""
    if not projects_data:
        print("No projects found or error occurred")
        return
    
    print(f"Projects for {REPO_OWNER}/{REPO_NAME}:")
    print("-" * 50)
    
    # Process new projects (ProjectV2)
    new_projects = projects_data["projectsV2"]["nodes"]
    for project in new_projects:
        print(f"• Name: {project['title']}")
        print(f"  Number: #{project['number']}")
        print(f"  Type: New Project (ProjectV2)")
        print("-" * 30)
    
    # Process classic projects
    classic_projects = projects_data["projects"]["nodes"]
    for project in classic_projects:
        print(f"• Name: {project['name']}")
        print(f"  Number: #{project['number']}")
        print(f"  Type: Classic Project (sunset on 2024-08-23) :cite[3]")
        print("-" * 30)

if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print("Error: GitHub token not found in GITHUB_PAT environment variable")
        print("Create token with permissions: repo, read:project")
    else:
        projects_data = get_github_projects()
        print_project_details(projects_data)
