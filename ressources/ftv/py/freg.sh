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

frha_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037721\/F3_RhoneAlpes/g')
fauv_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037600\/F3_Auvergne/g')
falp_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037536\/F3_Alpes/g')
fbog_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037704\/F3_Bourgogne/g')
ffrc_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037709\/F3_FrancheComte/g')
fbre_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037705\/F3_Bretagne/g')
fctr_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037706\/F3_Centre/g')
fcrs_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037708\/F3_Corse/g')
fals_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037598\/F3_Alsace/g')
fchg_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037707\/F3_Champagne/g')
flor_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037713\/F3_Lorraine/g')
fpdc_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037715\/F3_Nord_PDC/g')
fpcd_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037718\/F3_Picardie/g')
fbnr_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037703\/F3_B_Normandie/g')
fhnr_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037710\/F3_H_Normandie/g')
faqt_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037599\/F3_Aquitaine/g')
flms_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037712\/F3_Limousin/g')
fpch_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037719\/F3_PoitouCharentes/g')
fmpr_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037714\/F3_MidiPyrenees/g')
fldr_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037711\/F3_Languedoc/g')
fpdl_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037717\/F3_Pays_Loire/g')
fpra_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037720\/F3_ProvenceAlpes/g')
fpca_content=$(cat "$input_file" | sed 's/2037716\/F3_Paris_IDF/2037702\/F3_Azur/g')


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
