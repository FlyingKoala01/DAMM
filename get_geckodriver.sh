#!/bin/bash

# Define the file and URL
FILE_NAME="geckodriver-v0.33.0-linux64.tar.gz"
URL="https://github.com/mozilla/geckodriver/releases/download/v0.33.0/$FILE_NAME"

# Check if the file exists
if [ ! -f "geckodriver" ]; then
    # File doesn't exist, so download it
    echo "Downloading geckodriver..."
    wget "$URL"

    # Uncompress the downloaded file
    tar -xvf "$FILE_NAME"

    # Delete the downloaded file
    rm "$FILE_NAME"
fi
