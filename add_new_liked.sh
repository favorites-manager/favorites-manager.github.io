#!/bin/bash

# Assign arguments to variables
source_file="new_liked.json"
destination_file="liked_vids.json"

# Remove the closing bracket from the destination file
sed -i '$ d' "$destination_file"
sed -i '$ d' "$destination_file"

# Append a comma to the destination file
echo -e "\t}," >> "$destination_file"

# Remove the opening bracket from the source file and append its contents to the destination file
sed '1d' "$source_file" >> "$destination_file"

echo "Successfully appended $source_file to $destination_file"

# Move images
mv new_liked/* liked
echo "Successfully moved images from new_liked to liked"