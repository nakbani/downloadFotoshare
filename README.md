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
