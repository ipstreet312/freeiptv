#!/bin/bash

content=$(<ressources/ftv/py/fr2.m3u8)

fr3_content=$(echo "$content" | sed 's/France_2/France_3/g; s/hls_fr2/hls_fr3/g')
fr4_content=$(echo "$content" | sed 's/France_2/France_4/g; s/hls_fr2/hls_fr4/g')
fr5_content=$(echo "$content" | sed 's/France_2/France_5/g; s/hls_fr2/hls_fr5/g')

echo "$fr3_content" > ressources/ftv/py/fr3.m3u8
echo "$fr4_content" > ressources/ftv/py/fr4.m3u8
echo "$fr5_content" > ressources/ftv/py/fr5.m3u8
