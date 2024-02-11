# Cloudflare Image Uploader

## Overview

The Cloudflare Image Uploader is a Python script designed to automate the bulk uploading of images to Cloudflare. It handles image uploads, manages duplicates by renaming, moves processed images to a designated directory, and generates a Markdown file listing all uploaded images for easy access and reference. This tool simplifies the management of web content images, especially for users with multiple images to upload and organize.

## Features

- **Bulk Uploads**: Automatically uploads multiple images to Cloudflare in one go.
- **Duplicate Handling**: Renames duplicate images to ensure uniqueness without overwriting existing files.
- **Processed Images Directory**: Moves images to a "processed" directory after successful upload.
- **Markdown Catalog Generation**: Creates a `.md` file listing all uploaded images with URLs, making it easy to incorporate images into web content.

## Prerequisites

- Python 3.6 or higher installed on your system.
- Cloudflare account and API token with permissions to upload images.
- Basic familiarity with Python and running scripts from the command line.

## Setup

1. **Clone or Download the Script**: Obtain the script files from the repository or download them directly to your local machine.

2. **Install Required Python Packages**:
   Open a terminal or command prompt and navigate to the script's directory. Install the required packages using pip:

   ```bash
   pip install requests

### Create a folder called Image_To_Be_Uploaded

add all the files and folder INSIDE cloudflare-image-upload folder into it


### Open the upload_img_py.py file and add your details 

Your settings

```bash
API_TOKEN = 'your_api_token'
ACCOUNT_ID = 'your_account_id'
IMAGES_DIRECTORY = 'X:\\Cloudflare Images\\Image_To_Be_Uploaded'
PROCESSED_DIRECTORY = 'X:\\Cloudflare Images\\Image_To_Be_Uploaded\\PROCESSED_DIRECTORY'
CATALOG_FILE_PATH = 'X:\\Cloudflare Images\\Image_To_Be_Uploaded\\image_catalog.md'
```

Edit Start_Image_upload.bat

add your path to python, unsure type in CMD type:  where python 
add your folder path to Image_To_Be_Uploaded

## Usage

### Windows
Double click the .bat file to run


### Linux 

python upload_img_cf.py


### markdown file

Check your markdown file for cloudflare url's 

Export as index.html and have all your images in a web browser to scroll through, right click to copy image url for pasting in your applications!



Pro Tip use notepad + + with Markdown viewer and just click export to html, double click html to open in web browser, find your image and right click save image link ( which is the cloudflare image url! 

---

<img src="https://imagedelivery.net/WfhVb8dSNAAvdXUdMfBuPQ/130577bc-512d-4a7e-9293-fe548d591700/public" alt="bot.png" width="256" />

