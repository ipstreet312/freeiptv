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
n12b_content=$(cat "$input_file" | sed 's#direct/hls/live/2033791/k12#n12/hls/live/2041434/n12_b#g; s/_2200/_850/g')
k12cc_content=$(cat "$input_file" | sed 's/k12/k12cc/g; s/2033791/2035325/g')

echo "$n12_content" > "$output_dir/n12.m3u8"
echo "$n12b_content" > "$output_dir/n12b.m3u8"
echo "$k12cc_content" > "$output_dir/k12cc.m3u8"
