import os
from github import Github

# Set up GitHub token and organization/user details
GITHUB_TOKEN = "your_github_token"
ORG_NAME = "your_org_or_user_name"

# Initialize GitHub API client
g = Github(GITHUB_TOKEN)
org = g.get_organization(ORG_NAME)

# Define build stack identifiers
STACK_FILES = {
    "Maven": ["pom.xml"],
    "Gradle": ["build.gradle", "build.gradle.kts"],
    "Ant": ["build.xml"],
    "Python": ["requirements.txt", "setup.py", "Pipfile", "pyproject.toml"],
    "Node.js": ["package.json"],
    "Go": ["go.mod"],
    "DotNet": [".csproj", ".vbproj", ".sln"]
}

def identify_stack(repo_name):
    """Identify the stack for a repository."""
    repo = org.get_repo(repo_name)
    contents = repo.get_contents("")
    stack = set()
    
    # Analyze files in the repository
    for file in contents:
        for stack_name, identifiers in STACK_FILES.items():
            if any(file.name.endswith(identifier) for identifier in identifiers):
                stack.add(stack_name)
    
    # Convert to a list for return
    return list(stack)

def main():
    """Main function to process repositories."""
    repos = org.get_repos()
    result = {}
    
    for repo in repos:
        print(f"Analyzing {repo.name}...")
        stack = identify_stack(repo.name)
        if len(stack) > 1:
            stack.insert(0, "Multiple Stacks Detected")  # Add a warning for multiple stacks
        result[repo.name] = stack
    
    # Print the results
    for repo_name, stack in result.items():
        print(f"{repo_name}: {', '.join(stack)}")

if __name__ == "__main__":
    main()
