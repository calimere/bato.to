# Bato.to Downloader

This project is a Python script designed to download manga chapters from the [Bato.to](https://bato.to) website, save the images locally, and convert them into CBZ files.

## Features

- Extract chapter links from a series URL.
- Download images for each chapter.
- Create CBZ files for each chapter.

## Prerequisites

- Python 3.x
- The following libraries must be installed:
    - `requests`
    - `re` (included in the standard library)
    - `os` (included in the standard library)
    - `zipfile` (included in the standard library)

## Installation

1. Clone this repository or copy the script to a local file.
2. Install the required dependencies using the following command:
     ```bash
     pip install requests
     ```

## Usage

1. Run the Python script:
     ```bash
     python run.py
     ```
2. Enter the series URL you want to download (or leave it blank to use the default URL).
3. The script will download the chapters and create CBZ files in the `cbz` folder.

## Code Structure

### Main Functions

- **`extract_href_and_b_content(url)`**  
    Extracts chapter links and their titles from a series URL.

- **`download_images_from_chapter(url, chapter_number)`**  
    Downloads the images of a chapter and saves them in a dedicated folder.

- **`create_cbz_from_directory(directory_name)`**  
    Creates a CBZ file from the images in a folder.

### Main Flow

1. The user provides a series URL.
2. Chapters are extracted and downloaded.
3. Images are converted into CBZ files.

## Warnings

- This script is intended for personal use only. Make sure to comply with Bato.to's terms of service.
- Performance may vary depending on chapter size and your internet connection speed.

## Contribution

Contributions are welcome! Feel free to open an issue or a pull request to improve this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.