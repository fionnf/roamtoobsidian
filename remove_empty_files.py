import os

# Define the path to the vault
path = '/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/My Drive/Roam to Obsidian/Roam_proc/'  # Make sure the path ends with a slash

# Use os.path.join to handle file paths
vaultDir = path
files = os.listdir(vaultDir)

for file in files:
    file_path = os.path.join(vaultDir, file)  # Construct the full file path
    # Check if the file exists and if its size is 0
    if os.path.exists(file_path) and os.stat(file_path).st_size == 0:
        os.remove(file_path)
        print(f"Deleted empty file: {file}")