#!/bin/bash

# Specify the source and destination directories
source_directory="json/"
destination_directory="movie/"

# Iterate over each file in the source directory
for file in "${source_directory}"*; do
    # Move the file to the destination directory
    mv "$file" "${destination_directory}"
    echo "File '$file' moved to '${destination_directory}'"
done

# Print the result
echo "All files moved from '${source_directory}' to '${destination_directory}'"
