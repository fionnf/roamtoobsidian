import os

# Specify the root directory where your notes are stored
notesDir = '/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/My Drive/Roam to Obsidian/Roam_proc/'  # Make sure the path ends with a slash

#remove notes with the following in them
expletive = '**CRM**'

# Walk through all files in all directories within the specified notes directory
for subdir, dirs, files in os.walk(notesDir):
    for file in files:
        file_path = os.path.join(subdir, file)

        # Check if the file is a Markdown file
        if file.endswith('.md'):
            with open(file_path, 'r', errors='ignore') as f:
                content = f.read()
                # If the content contains [[CRM]], delete the file
                if expletive in content:
                    print(f"Deleting file: {file_path}")
                    os.remove(file_path)