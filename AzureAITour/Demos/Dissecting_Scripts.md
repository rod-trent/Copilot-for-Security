## Demo: Dissecting Scripts

```
Dissect the following script and tell me if it is potentially dangerous

# PowerShell Script to Create Multiple Files

# Specify the target directory where files will be created
$targetDirectory = "C:\TestFiles"

# Specify the number of files to create
$numberOfFiles = 1000 # Adjust this number as needed

# Specify the base name for the files
$baseFileName = "TestFile"

# Specify the file extension
$fileExtension = ".txt"

# Check if the target directory exists, if not, create it
if (-not (Test-Path -Path $targetDirectory)) {
    New-Item -ItemType Directory -Path $targetDirectory
}

# Create the files
for ($i = 1; $i -le $numberOfFiles; $i++) {
    $fileName = "$baseFileName$i$fileExtension"
    $filePath = Join-Path -Path $targetDirectory -ChildPath $fileName
    # Create an empty file
    New-Item -ItemType File -Path $filePath -Force
}

Write-Host "Created $numberOfFiles files in '$targetDirectory'."
```
---

