import os

# Specify the root directory where your Markdown files are stored
filesDir = '/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/My Drive/Roam to Obsidian/Roam_proc/'  # Ensure the path ends with a slash

# Walk through all files in all directories within the specified directory
for subdir, dirs, files in os.walk(filesDir):
    for file in files:
        # Only process files ending with .md
        if file.endswith('.md'):
            file_path = os.path.join(subdir, file)

            # Open and read the file content
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()

            # Replace all instances of $$ with $
            new_content = content.replace('$$', '$')

            # Write the new content back to the file if changes were made
            if new_content != content:
                with open(file_path, 'w') as f:
                    f.write(new_content)
                print(f"Updated file: {file_path}")