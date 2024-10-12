#!/bin/bash

input_file="ressources/ftv/py/fidf.m3u8"
output_dir="ressources/ftv/py"

if [ ! -f "$input_file" ]; then
    echo "Input file $input_file not found!"
    exit 1
fi

if [ ! -d "$output_dir" ]; then
    echo "Output directory $output_dir not found!"
    exit 1
fi

frha_content=$(cat "$input_file" | sed 's/paris/rhone-alpes/g')
fauv_content=$(cat "$input_file" | sed 's/paris/auvergne/g')
falp_content=$(cat "$input_file" | sed 's/paris/alpes/g')
fbog_content=$(cat "$input_file" | sed 's/paris/bourgogne/g')
ffrc_content=$(cat "$input_file" | sed 's/paris/franche-comte/g')
fbre_content=$(cat "$input_file" | sed 's/paris/bretagne/g')
fctr_content=$(cat "$input_file" | sed 's/paris/centre/g')
fcrs_content=$(cat "$input_file" | sed 's/paris/corse/g')
fals_content=$(cat "$input_file" | sed 's/paris/alsace/g')
fchg_content=$(cat "$input_file" | sed 's/paris/champagne/g')
flor_content=$(cat "$input_file" | sed 's/paris/lorraine/g')
fpdc_content=$(cat "$input_file" | sed 's/paris/nordpdc/g')
fpcd_content=$(cat "$input_file" | sed 's/paris/picardie/g')
fbnr_content=$(cat "$input_file" | sed 's/paris/basse-normandie/g')
fhnr_content=$(cat "$input_file" | sed 's/paris/haute-normandie/g')
faqt_content=$(cat "$input_file" | sed 's/paris/aquitaine/g')
flms_content=$(cat "$input_file" | sed 's/paris/limousin/g')
fpch_content=$(cat "$input_file" | sed 's/paris/poitou-charentes/g')
fmpr_content=$(cat "$input_file" | sed 's/paris/midi-pyrenees/g')
fldr_content=$(cat "$input_file" | sed 's/paris/languedoc/g')
fpdl_content=$(cat "$input_file" | sed 's/paris/pays-loire/g')
fpra_content=$(cat "$input_file" | sed 's/paris/provence-alpes/g')
fpca_content=$(cat "$input_file" | sed 's/paris/cote-dazur/g')


echo "$frha_content" > "$output_dir/frha.m3u8"
echo "$fauv_content" > "$output_dir/fauv.m3u8"
echo "$falp_content" > "$output_dir/falp.m3u8"
echo "$fbog_content" > "$output_dir/fbog.m3u8"
echo "$ffrc_content" > "$output_dir/ffrc.m3u8"
echo "$fbre_content" > "$output_dir/fbre.m3u8"
echo "$fctr_content" > "$output_dir/fctr.m3u8"
echo "$fcrs_content" > "$output_dir/fcrs.m3u8"
echo "$fals_content" > "$output_dir/fals.m3u8"
echo "$fchg_content" > "$output_dir/fchg.m3u8"
echo "$flor_content" > "$output_dir/flor.m3u8"
echo "$fpdc_content" > "$output_dir/fpdc.m3u8"
echo "$fpcd_content" > "$output_dir/fpcd.m3u8"
echo "$fbnr_content" > "$output_dir/fbnr.m3u8"
echo "$fhnr_content" > "$output_dir/fhnr.m3u8"
echo "$faqt_content" > "$output_dir/faqt.m3u8"
echo "$flms_content" > "$output_dir/flms.m3u8"
echo "$fpch_content" > "$output_dir/fpch.m3u8"
echo "$fmpr_content" > "$output_dir/fmpr.m3u8"
echo "$fldr_content" > "$output_dir/fldr.m3u8"
echo "$fpdl_content" > "$output_dir/fpdl.m3u8"
echo "$fpra_content" > "$output_dir/fpra.m3u8"
echo "$fpca_content" > "$output_dir/fpca.m3u8"
