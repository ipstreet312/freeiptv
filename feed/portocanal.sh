#!/bin/bash
# Thanks to LITUATUI user on github
cd feed

python porto_canal.py && sed -e '/x8egnb8/ {' -e 'r porto_canal.txt' -e 'd' -e '}' -i portocanal.m3u8

exit 0
