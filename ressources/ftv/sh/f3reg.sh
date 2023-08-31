#!/bin/bash

curl -s "https://live-regions-p.ftven.fr/ZXh0/hls/live/2037716/F3_Paris_IDF/index.m3u8" > /ressources/ftv/sh/f3reg.txt

replacement_value=$(grep -o 'ftven\.fr/\(.*\)/hls' /ressources/ftv/sh/f3reg.txt | sed 's/ftven\.fr\///;s/\/hls//')

sed -i "s|ftven.fr/.*?/hls|ftven.fr/$replacement_value/hls|g" all.m3u
