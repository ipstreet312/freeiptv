#!/bin/bash

wget -qO f3reg.txt "https://hdfauth.ftven.fr/esi/TA?url=https://live-regions-p.ftven.fr/hls/live/2037716/F3_Paris_IDF/index.m3u8"

replacement_value=$(grep -o 'ftven\.fr/\(.*\)/hls' f3reg.txt | sed 's/ftven\.fr\///;s/\/hls//')

sed -i "s|ftven.fr/.*?/hls|ftven.fr/$replacement_value/hls|g" all.m3u
