#!/bin/bash

replacement_value=$(wget -qO - "https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/ftv/py/f3reg.txt" | grep -o 'ftven\.fr/\(.*\)/hls' | sed 's/ftven\.fr\///;s/\/hls//')

sed -i "s|ftven.fr/.*?/hls|ftven.fr/$replacement_value/hls|g" all.m3u

exit 0
