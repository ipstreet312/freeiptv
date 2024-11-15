#!/bin/bash

input_file="ressources/ftv/py/fr2.m3u8"
output_dir="ressources/ftv/py"

if [ ! -f "$input_file" ]; then
    echo "Input file $input_file not found!"
    exit 1
fi

if [ ! -d "$output_dir" ]; then
    echo "Output directory $output_dir not found!"
    exit 1
fi

fr3_content=$(cat "$input_file" | sed 's/France_2/France_3/g; s/hls_fr2/hls_fr3/g')
fr4_content=$(cat "$input_file" | sed 's/France_2/France_4/g; s/hls_fr2/hls_fr4/g')
fr5_content=$(cat "$input_file" | sed 's/France_2/France_5/g; s/hls_fr2/hls_fr5/g')
noa_content=$(cat "$input_file" | sed 's/France_2/Regions_noa/g; s/hls_fr2/hls_noa/g')
fri_content=$(cat "$input_file" | sed 's/France_2/France_Info/g; s/hls_fr2/hls_monde_frinfo/g')
arte_content=$(cat "$input_file" | sed 's/France_2/Arte/g; s/-p/-frmedias-p/g; s/hls_fr2/hls_arte/g')
fr1wf_content=$(cat "$input_file" | sed 's/France_2/1er_Wallis_Futuna/g; s/hls_fr2/hls_1er_WF/g')
fr1wfm_content=$(cat "$input_file" | sed 's/France_2/1er_Wallis_Futuna/g; s/hls_fr2/hls_monde_1er_WF/g')
fr1spm_content=$(cat "$input_file" | sed 's/France_2/1er_Saint-Pierre_Miquelon/g; s/hls_fr2/hls_1er_SPM/g')
fr1spmm_content=$(cat "$input_file" | sed 's/France_2/1er_Saint-Pierre_Miquelon/g; s/hls_fr2/hls_monde_1er_SPM/g')
fr1pol_content=$(cat "$input_file" | sed 's/France_2/1er_Polynesie/g; s/hls_fr2/hls_1er_Polynesie/g')
fr1polm_content=$(cat "$input_file" | sed 's/France_2/1er_Polynesie/g; s/hls_fr2/hls_monde_1er_Polynesie/g')
fr1mar_content=$(cat "$input_file" | sed 's/France_2/1er_Martinique/g; s/hls_fr2/hls_1er_Mar/g')
fr1marm_content=$(cat "$input_file" | sed 's/France_2/1er_Martinique/g; s/hls_fr2/hls_monde_1er_Mar/g')
fr1gua_content=$(cat "$input_file" | sed 's/France_2/1er_Guadeloupe/g; s/hls_fr2/hls_1er_Gua/g')
fr1guam_content=$(cat "$input_file" | sed 's/France_2/1er_Guadeloupe/g; s/hls_fr2/hls_monde_1er_Gua/g')
fr1guy_content=$(cat "$input_file" | sed 's/France_2/1er_Guyane/g; s/hls_fr2/hls_1er_Guy/g')
fr1guym_content=$(cat "$input_file" | sed 's/France_2/1er_Guyane/g; s/hls_fr2/hls_monde_1er_Guy/g')
fr1may_content=$(cat "$input_file" | sed 's/France_2/1er_Mayotte/g; s/hls_fr2/hls_1er_May/g')
fr1maym_content=$(cat "$input_file" | sed 's/France_2/1er_Mayotte/g; s/hls_fr2/hls_monde_1er_May/g')
fr1nc_content=$(cat "$input_file" | sed 's/France_2/1er_Nouvelle_Caledonie/g; s/hls_fr2/hls_1er_NC/g')
fr1ncm_content=$(cat "$input_file" | sed 's/France_2/1er_Nouvelle_Caledonie/g; s/hls_fr2/hls_monde_1er_NC/g')
fr1reu_content=$(cat "$input_file" | sed 's/France_2/1er_Reunion/g; s/hls_fr2/hls_1er_Reu/g')
fr1reum_content=$(cat "$input_file" | sed 's/France_2/1er_Reunion/g; s/hls_fr2/hls_monde_1er_Reu/g')
fr1nc2_content=$(cat "$input_file" | sed 's/France_2/1er_Nouvelle_Caledonie/g; s/hls_fr2/hls_1er/g')
fr1ncm2_content=$(cat "$input_file" | sed 's/France_2/1er_Nouvelle_Caledonie/g; s/hls_fr2/hls_monde_1er/g')
fr1ncm3_content=$(cat "$input_file" | sed 's/France_2/1er_Nouvelle_Caledonie/g; s/hls_fr2/hls_monde/g')
fr1reu2_content=$(cat "$input_file" | sed 's/France_2/1er_Reunion/g; s/hls_fr2/hls_1er/g')
fr1reum2_content=$(cat "$input_file" | sed 's/France_2/1er_Reunion/g; s/hls_fr2/hls_monde_1er/g')
fr1reum3_content=$(cat "$input_file" | sed 's/France_2/1er_Reunion/g; s/hls_fr2/hls_monde/g')

echo "$fr3_content" > "$output_dir/fr3.m3u8"
echo "$fr4_content" > "$output_dir/fr4.m3u8"
echo "$fr5_content" > "$output_dir/fr5.m3u8"
echo "$noa_content" > "$output_dir/fnoa.m3u8"
echo "$fri_content" > "$output_dir/frin.m3u8"
echo "$arte_content" > "$output_dir/frarte.m3u8"
echo "$fr1wf_content" > "$output_dir/fr1wf.m3u8"
echo "$fr1wfm_content" > "$output_dir/fr1wfm.m3u8"
echo "$fr1spm_content" > "$output_dir/fr1spm.m3u8"
echo "$fr1spmm_content" > "$output_dir/fr1spmm.m3u8"
echo "$fr1mar_content" > "$output_dir/fr1mar.m3u8"
echo "$fr1marm_content" > "$output_dir/fr1marm.m3u8"
echo "$fr1gua_content" > "$output_dir/fr1gua.m3u8"
echo "$fr1guam_content" > "$output_dir/fr1guam.m3u8"
echo "$fr1guy_content" > "$output_dir/fr1guy.m3u8"
echo "$fr1guym_content" > "$output_dir/fr1guym.m3u8"
echo "$fr1may_content" > "$output_dir/fr1may.m3u8"
echo "$fr1maym_content" > "$output_dir/fr1maym.m3u8"
echo "$fr1nc_content" > "$output_dir/fr1nc.m3u8"
echo "$fr1ncm_content" > "$output_dir/fr1ncm.m3u8"
echo "$fr1reu_content" > "$output_dir/fr1reu.m3u8"
echo "$fr1reum_content" > "$output_dir/fr1reum.m3u8"
echo "$fr1pol_content" > "$output_dir/fr1pol.m3u8"
echo "$fr1polm_content" > "$output_dir/fr1polm.m3u8"
echo "$fr1nc2_content" > "$output_dir/fr1nc2.m3u8"
echo "$fr1ncm2_content" > "$output_dir/fr1ncm2.m3u8"
echo "$fr1ncm3_content" > "$output_dir/fr1ncm3.m3u8"
echo "$fr1reu2_content" > "$output_dir/fr1reu2.m3u8"
echo "$fr1reum2_content" > "$output_dir/fr1reum2.m3u8"
echo "$fr1reum3_content" > "$output_dir/fr1reum3.m3u8"
