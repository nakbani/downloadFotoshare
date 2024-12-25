import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

# Setup
chrome_driver_path = "C:/Users/xxxx/Documents/chromedriver.exe"  # Update with your ChromeDriver path
url = ""  # Update with your fotoshare URL

# Initialize WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

# Allow some time for the page to load
time.sleep(5)

# Locate all the items we want to download by their thumbnail
try:
    thumbnail_elements = driver.find_elements(By.CSS_SELECTOR, "div.thumb.border-radius-thumb")
    print(f"Found {len(thumbnail_elements)} items to download.")
except Exception as e:
    print(f"Error finding thumbnails: {e}")
    driver.quit()
    exit()

# Setup download and folder paths
downloads_folder = r"C:\Users\xxxx\Downloads"  # Replace with your downloads folder path
fotoshare_folder = r"C:\Users\xxxx\Documents\Fotoshare Pictures" # Replace with the folder you want to save to - this folder must already exist

# Loop through each thumbnail
for thumb_index, thumbnail in enumerate(thumbnail_elements):
    try:
        # Scroll the thumbnail into view, if it's not in view already
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", thumbnail)
        time.sleep(1)  # Allow time for scrolling
        
        # Attempt to click the thumbnail
        try:
            thumbnail.click()  # Open the thumbnail
        except ElementClickInterceptedException:
            print(f"Element {thumb_index} not clickable, retrying after scrolling.")
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", thumbnail)
            time.sleep(1)
            thumbnail.click()
        
        time.sleep(2)  # Allow time for the gallery to load

        # Locate swiper container which contains all the files we want to download
        swiper_container = driver.find_element(By.ID, "thumb-swiper-container")
        swiper_items = swiper_container.find_elements(By.CLASS_NAME, "swiper-slide")
        print(f"Item {thumb_index + 1}: Found {len(swiper_items)} files to download.")

        # New list to track downloaded files for each thumbnail for when we want to move it to its own folder
        downloaded_files = []

        # Loop through each file we want to download
        for index in range(len(swiper_items)):
            try:
                # Click the download button
                download_button = driver.find_element(By.ID, "sessionItemDownloadButton")
                print(f"Clicking download button for file {index + 1}.")
                download_button.click()
                time.sleep(1)  # Allow time for the download to complete

                # Identify the most recently downloaded file by timestamp
                recent_file = sorted(
                    [f for f in os.listdir(downloads_folder) if f.endswith('.jpg') or f.endswith('.mp4')],
                    key=lambda f: os.path.getmtime(os.path.join(downloads_folder, f)),
                    reverse=True
                )[:1]

                if recent_file:  # Ensure there is a file
                    downloaded_files.append(recent_file[0])  # Append the file name directly (not a list)

                # Click the "Next" button to navigate to the next image, if we haven't reached the last image/gif yet
                if index < len(swiper_items) - 1:
                    next_button = driver.find_element(By.CLASS_NAME, "swiper-button-next")
                    print(f"Navigating to the next item {index + 2}.")
                    next_button.click()
                    time.sleep(1)  # Allow time for the next image to load

                # Close the current thumbnail so that we can move onto the next one
                elif index == len(swiper_items) - 1:
                    close_button = driver.find_element(By.ID, "albumBackButton")
                    print(f"Closing the thumbnail.")
                    close_button.click()
                    time.sleep(1)  # Allow time to return to the thumbnails

            except Exception as e:
                print(f"Error processing item {index + 1}: {e}")

        # Identify the folder we want to move the last downloaded files to (thumbnail number)
        folder_path = os.path.join(fotoshare_folder, str(thumb_index + 1))

        # Check if the folder exists, if not, create it and name it according to the thumbnail number (1, 2, 3...)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")

        for file_name in downloaded_files:
            # Find the file we want to move
            src_file = os.path.join(downloads_folder, file_name)
            if os.path.exists(src_file):  # Check if file exists before moving
                dst_file = os.path.join(folder_path, file_name) # Declare where we want to move it to
                try:
                    # Move file to the appropriate folder
                    shutil.move(src_file, dst_file) # Move the file we want to move to the specified directory
                    print(f"Moved {file_name} to {folder_path}")
                except Exception as e:
                    print(f"Error moving file {file_name}: {e}")

    except Exception as thumb_error:
        print(f"Error processing thumbnail {thumb_index + 1}: {thumb_error}")

# Close the browser and print a success message if all files were downloaded successfully
driver.quit()
print("All images downloaded.")
