import requests
import csv

# Define the base URL for the GitHub API and the repository
base_url = "https://api.github.com/repos"
owner = "OWNER"
repo = "REPO"
repo_url = f"https://github.com/{owner}/{repo}/blob/main"

# Make a GET request to the GitHub API
response = requests.get(f"{base_url}/{owner}/{repo}/git/trees/main?recursive=1")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Open a CSV file in write mode
    with open(f'{repo}_file_structure.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(["Type", "Path", "URL"])

        # Write the file and directory names, paths and URLs
        for item in data['tree']:
            if item['type'] == 'blob':  # Only files have URLs, not directories
                url = f"{repo_url}/{item['path']}"
            else:
                url = ''
            writer.writerow([item['type'], item['path'], url])
else:
    print(f"Failed to fetch data from GitHub API. Status code: {response.status_code}")
