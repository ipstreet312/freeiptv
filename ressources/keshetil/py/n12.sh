#!/bin/bash

input_file="ressources/keshetil/py/k12.m3u8"
output_dir="ressources/keshetil/py"

if [ ! -f "$input_file" ]; then
    echo "Input file $input_file not found!"
    exit 1
fi

if [ ! -d "$output_dir" ]; then
    echo "Output directory $output_dir not found!"
    exit 1
fi

n12_content=$(cat "$input_file" | sed 's/direct/n12/g; s/2033791/2103938/g')

echo "$n12_content" > "$output_dir/n12.m3u8"
