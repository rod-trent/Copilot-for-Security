import pandas as pd
import json

# Prompt for the JSON file and the path
json_file = input("Enter the path to the JSON file: ")
csv_file = input("Enter the path to the output CSV file: ")

# Load the JSON data
with open(json_file, 'r') as f:
    data = json.load(f)["objects"]

# Initialize a list to store the DataFrames
dfs = []

# Iterate over the data
for d in data:
    # Check if the 'external_references' key exists
    if 'external_references' in d:
        # Flatten the dictionary and append the DataFrame to the list
        dfs.append(pd.json_normalize(d, record_path='external_references', 
                                      meta=['name', 'description', 'x_mitre_shortname', 'created_by_ref', 
                                            'object_marking_refs', 'type', 'id', 'created', 'modified'], 
                                      record_prefix='external_references.', errors='ignore'))

# Concatenate all the DataFrames in the list
df = pd.concat(dfs, ignore_index=True)

# Write the DataFrame to a CSV file
df.to_csv(csv_file, index=False)
