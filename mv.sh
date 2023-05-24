#!/bin/bash

folder="TMDB/json"  # Replace with the actual folder path

# Loop through the files in the folder
for file in "$folder"/*; do
    # echo "$file"
    mv $file json/
done
