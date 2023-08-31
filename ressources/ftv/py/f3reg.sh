#!/bin/bash

replacement_value=$(grep -o 'live-regions-p\.ftven\.fr/\(.*\)/hls' ressources/ftv/py/f3reg.txt | sed 's/live-regions-p\.ftven\.fr\///;s/\/hls//')

sed -i "s|live-regions-p.ftven.fr/ZXhDQ4|live-regions-p.ftven.fr/$replacement_value|g" all.m3u
