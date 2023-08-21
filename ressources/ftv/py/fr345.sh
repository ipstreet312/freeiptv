#!/bin/bash

content=$(<ressources/ftv/py/fr2.m3u8)

fr3_content="${content/France_2/France_3}"
fr3_content="${fr3_content/hls_fr2/hls_fr3}"
echo "$fr3_content" > ressources/ftv/py/fr3.m3u8

fr4_content="${content/France_2/France_4}"
fr4_content="${fr4_content/hls_fr2/hls_fr4}"
echo "$fr4_content" > ressources/ftv/py/fr4.m3u8

fr5_content="${content/France_2/France_5}"
fr5_content="${fr5_content/hls_fr2/hls_fr5}"
echo "$fr5_content" > ressources/ftv/py/fr5.m3u8
