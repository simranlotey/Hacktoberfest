#!/bin/bash
# Calculte the size of a directory

echo "Enter directory path:"
read dirpath
total_size=$(du -sh $dirpath | cut -f1)
echo "Total size of $dirpath: $total_size"
