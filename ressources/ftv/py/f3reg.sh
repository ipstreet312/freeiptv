#!/bin/bash

new_string_variable=$(grep -o 'https://live-regions-p\.ftven\.fr/\(.*\)/hls/live' ressources/ftv/py/f3reg.txt | sed 's|https://live-regions-p\.ftven\.fr/||;s|/hls/live||')

sed -i "s|live-regions-p.ftven.fr/[^/]*|live-regions-p.ftven.fr/$new_string_variable|g" all.m3u
