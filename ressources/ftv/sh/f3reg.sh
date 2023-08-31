#!/bin/bash

replacement_value=$(wget -qO - "https://hdfauth.ftven.fr/esi/TA?url=https://live-regions-p.ftven.fr/hls/live/2037716/F3_Paris_IDF/index.m3u8" | grep -o 'ftven\.fr/\(.*\)/hls' | sed 's/ftven\.fr\///;s/\/hls//')

sed -i "s|ftven.fr/.*?/hls|ftven.fr/$replacement_value/hls|g" all.m3u
