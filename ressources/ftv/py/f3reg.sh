#!/bin/bash

replacement_value=$(grep -o 'ftven\.fr/\(.*\)/hls' ressources/ftv/py/f3reg.txt | sed 's/ftven\.fr\///;s/\/hls//')

sed -i "s|ftven.fr/.*?/hls|ftven.fr/$replacement_value/hls|g" all.m3u
