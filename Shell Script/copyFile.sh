#!/bin/bash
# Copy a file in [new] directory (location)

echo "Enter source file: "
read source

echo "Enter destination file: "
read dest

cp $source $dest
echo "File copied successfully!"