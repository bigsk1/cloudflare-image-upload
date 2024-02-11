import requests
import os
import shutil
import json
import logging

# Configure logging
logging.basicConfig(filename='upload_errors.log', level=logging.ERROR)

# Your settings
API_TOKEN = 'your_api_token'
ACCOUNT_ID = 'your_account_id'
IMAGES_DIRECTORY = 'X:\\Cloudflare Images\\Image_To_Be_Uploaded'
PROCESSED_DIRECTORY = 'X:\\Cloudflare Images\\Image_To_Be_Uploaded\\PROCESSED_DIRECTORY'
CATALOG_FILE_PATH = 'X:\\Cloudflare Images\\Image_To_Be_Uploaded\\image_catalog.md'

if not os.path.exists(PROCESSED_DIRECTORY):
    os.makedirs(PROCESSED_DIRECTORY)

headers = {
    'Authorization': f'Bearer {API_TOKEN}',
}

new_catalog_entries = []
successful_uploads = 0

print("Starting image uploads...")

for filename in os.listdir(IMAGES_DIRECTORY):
    if filename.endswith((".png", ".jpg", ".jpeg")):
        print(f"Uploading {filename}...")
        file_path = os.path.join(IMAGES_DIRECTORY, filename)
        with open(file_path, 'rb') as file:
            files = {'file': file}
            try:
                response = requests.post(f'https://api.cloudflare.com/client/v4/accounts/{ACCOUNT_ID}/images/v1', headers=headers, files=files)
                response.raise_for_status()
                response_data = response.json()
                image_url = response_data['result']['variants'][0]
                new_catalog_entries.append(f"{filename}|{image_url}")
                successful_uploads += 1
                print(f"Successfully uploaded {filename}.")
            except requests.exceptions.RequestException as e:
                error_message = f"Failed to upload {filename}: {e}"
                logging.error(error_message)
                print(error_message)
                continue
        
        shutil.move(file_path, os.path.join(PROCESSED_DIRECTORY, filename))

if new_catalog_entries:
    with open(CATALOG_FILE_PATH, 'a') as catalog_file:
        for entry in new_catalog_entries:
            filename, image_url = entry.split('|')
            catalog_file.write(f'<img src="{image_url}" alt="{filename}" width="256" />\n\n')

# Log the total number of successful uploads
logging.info(f"Successfully uploaded {successful_uploads} files.")

if successful_uploads > 0:
    print(f"Upload complete. Successfully uploaded {successful_uploads} files.")
else:
    print("No files were uploaded.")
