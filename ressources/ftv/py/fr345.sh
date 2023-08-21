#!/bin/bash

content=$(<ressources/ftv/py/fr2.m3u8)

fr3_content="${content/France_2/France_3}"
fr3_content="${fr3_content/hls_fr2/hls_fr3}"
echo "$fr3_content" > ressources/ftv/py/fr3.m3u8
