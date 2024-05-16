# Define the base URL for the GitHub API and the repository
$base_url = "https://api.github.com/repos"
$owner = "OWNER"
$repo = "REPO"
$repo_url = "https://github.com/$owner/$repo/blob/main"

# Make a GET request to the GitHub API
$response = Invoke-RestMethod -Uri "$base_url/$owner/$repo/git/trees/main?recursive=1"

# Create a CSV file and write the header
"Type,Path,URL" | Out-File -FilePath "$repo`_file_structure.csv"

# Write the file and directory names, paths and URLs
foreach ($item in $response.tree) {
    if ($item.type -eq 'blob') {  # Only files have URLs, not directories
        $url = "$repo_url/$($item.path)"
    } else {
        $url = ''
    }
    "$($item.type),$($item.path),$url" | Out-File -FilePath "$repo`_file_structure.csv" -Append
}
