# Fotoshare Downloader Script

## Overview

This Python script automates the process of downloading images and videos from a Fotoshare gallery and organizing them into folders based on the thumbnail index. The script uses Selenium WebDriver to interact with a Fotoshare URL, click on thumbnails to view the gallery, and download the associated images or videos (.jpg, .mp4). Once the files are downloaded, they are moved into specific folders named according to the thumbnail index.

## Features

- **Automated Downloading:** The script automatically navigates through a Fotoshare gallery, clicks on each thumbnail, and downloads the corresponding media files (images or videos).
- **File Organization:** Downloaded files are moved into dedicated folders named after the thumbnail index (e.g., `Fotoshare Pictures/1`, `Fotoshare Pictures/2`).
- **Error Handling:** Handles various errors, such as unclickable elements or failed downloads, and retries when necessary.
- **Flexible File Types:** By default, the script looks for `.jpg` and `.mp4` files, but this can be easily modified for other file types.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver (Make sure to download the appropriate version for your Chrome browser)
- Web browser (Google Chrome)
  
### Installation

1. **Install Python dependencies:**

   ```bash
   pip install selenium
2. ### Download ChromeDriver:

- Download the correct version of ChromeDriver based on your browser version from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Make sure to place the `chromedriver.exe` file in the appropriate path (update `chrome_driver_path` in the script).

3. ### Update Folder Paths:

- In the script, set the `downloads_folder` to your default downloads folder path.
- Set the `fotoshare_folder` to the folder where you want to save the downloaded images and videos.

## Usage

1. ### Edit the Script:

- Update the `chrome_driver_path` with the path to your `chromedriver.exe`.
- Set the `url` variable to the Fotoshare gallery URL that you want to scrape.
- Modify the `downloads_folder` and `fotoshare_folder` variables to match your local paths.

2. ### Run the Script:

```bash
python fotoshare_downloader.py
