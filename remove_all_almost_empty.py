import os

# Specify the root directory where your files are stored
filesDir = '/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/My Drive/Roam to Obsidian/Roam_proc/'  # Ensure the path ends with a slash

# Walk through all files in all directories within the specified directory
for subdir, dirs, files in os.walk(filesDir):
    for file in files:
        file_path = os.path.join(subdir, file)

        # Open and read the file content
        with open(file_path, 'r', errors='ignore') as f:
            content = f.read().strip()  # Read and strip any surrounding whitespace

            # Check if the content consists only of hyphens
            if set(content) == {'-'}:
                print(f"Deleting file: {file_path}")
                os.remove(file_path)