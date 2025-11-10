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
ch24_content=$(cat "$input_file" | sed 's#direct/hls/live/2033791/k12#direct/hls/live/2035340/ch24live#g; s/index_2200/video_7201280_p_1/g')
erets_content=$(cat "$input_file" | sed 's#direct/hls/live/2033791/k12#free/hls/live/2111419/erets/#g; s/index_2200/video_7201280_p_1/g')
savri_content=$(cat "$input_file" | sed 's#direct/hls/live/2033791/k12#free/hls/live/2111419/savri/#g; s/index_2200/video_7201280_p_1/g')
hatuna_content=$(cat "$input_file" | sed 's#direct/hls/live/2033791/k12#free/hls/live/2111419/hatuna/#g; s/index_2200/video_7201280_p_1/g')
kohav_content=$(cat "$input_file" | sed 's#direct/hls/live/2033791/k12#free/hls/live/2111419/kohav/#g; s/index_2200/video_7201280_p_1/g')
ninja_content=$(cat "$input_file" | sed 's#direct/hls/live/2033791/k12#free/hls/live/2111419/ninja/#g; s/index_2200/video_7201280_p_1/g')

echo "$n12_content" > "$output_dir/n12.m3u8"
echo "$n12b_content" > "$output_dir/n12b.m3u8"
echo "$k12cc_content" > "$output_dir/k12cc.m3u8"
echo "$ch24_content" > "$output_dir/ch24.m3u8"
echo "$erets_content" > "$output_dir/erets.m3u8"
echo "$savri_content" > "$output_dir/savri.m3u8"
echo "$hatuna_content" > "$output_dir/hatuna.m3u8"
echo "$kohav_content" > "$output_dir/kohav.m3u8"
echo "$ninja_content" > "$output_dir/ninja.m3u8"
