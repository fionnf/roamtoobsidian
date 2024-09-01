import re
import os
import requests
import calendar
import time
from io import BytesIO
import shutil

vaultDir = '/Users/fionnferreira/Library/CloudStorage/GoogleDrive-fionnferreira@gmail.com/My Drive/Roam to Obsidian/Roam_proc/'  # Ensure the path ends with a slash

i = 0  # Counter for naming downloaded files

# Walk through all files in all directories within the specified vault directory
for subdir, dirs, files in os.walk(vaultDir):
    for file in files:
        fileFullPath = os.path.join(subdir, file)
        with open(fileFullPath, 'r', errors='ignore') as fhand:
            file_data = fhand.readlines()  # Read file lines

        new_file_data = []
        modified = False

        for line in file_data:
            if 'firebasestorage' in line:
                try:
                    if '{{pdf:' in line:
                        link = re.search(r'https://firebasestorage(.*)\?alt(.*)\}', line)
                    else:
                        link = re.search(r'https://firebasestorage(.*)\?alt(.*)\)', line)

                    if link:
                        firebaseShort = 'https://firebasestorage' + link.group(1)
                        firebaseUrl = link.group(0)[:-1]

                        # Download the file
                        try:
                            r = requests.get(firebaseUrl)
                            r.raise_for_status()  # Check if the request was successful
                        except requests.exceptions.RequestException as e:
                            print(f"Failed to download {firebaseUrl}: {e}")
                            continue

                        # Create the assets folder if it doesn't exist
                        assets_folder = os.path.join(vaultDir, 'assets')
                        if not os.path.exists(assets_folder):
                            os.makedirs(assets_folder)

                        # Get the file extension
                        reg = re.search(r'(.*)\.(.+)', firebaseShort[-5:])
                        if reg:
                            ext = '.' + reg.group(2)
                        else:
                            ext = '.file'  # Default extension if not found

                        # Construct new file path
                        timestamp = calendar.timegm(time.gmtime())
                        newFilePath = os.path.join('assets', f'{timestamp}_{i}{ext}')

                        # Save the downloaded file
                        with open(os.path.join(vaultDir, newFilePath), 'wb') as output_file:
                            shutil.copyfileobj(BytesIO(r.content), output_file)

                        # Replace the Firebase URL with the new local file path in the line
                        line = line.replace(firebaseUrl, newFilePath)
                        modified = True
                        i += 1
                except AttributeError as e:
                    print(f"Regex error in file {fileFullPath}: {e}")
                    continue

            new_file_data.append(line)

        # If the file was modified, save the changes
        if modified:
            temp_file_path = os.path.join(vaultDir, f'temp_{file}')
            with open(temp_file_path, 'w', errors='ignore') as temp_file:
                temp_file.writelines(new_file_data)

            # Replace the original file with the temp file
            os.replace(temp_file_path, fileFullPath)

        print(f"Processed file: {fileFullPath}")