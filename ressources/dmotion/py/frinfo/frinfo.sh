#!/bin/bash

file_path="/ressources/dmotion/py/frinfo/frinfo.py"
file_directory=$(dirname "$file_path")

# Change the working directory to the file's directory
cd "$file_directory"

python frinfo.py > frinfo.m3u8

exit 0

#cd ressources/dmotion/py/frinfo
#python3 frinfo.py > frinfo.m3u8
#echo m3u grabbed
#exit 0
