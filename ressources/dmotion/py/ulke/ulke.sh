#!/bin/bash
# Thanks to LITUATUI user on github
cd ressources/dmotion/py/ulke

python ulke.py && sed -e '/x7yb4xm/ {' -e 'r ulke.txt' -e 'd' -e '}' -i ulke.m3u8

exit 0
