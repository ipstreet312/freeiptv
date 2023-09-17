#!/bin/bash
# Thanks to LITUATUI user on github
cd ressources/dmotion/py/pblsnt

python pblsnt.py && sed -e '/xkxbzc/ {' -e 'r pblsnt.txt' -e 'd' -e '}' -i pblsnt.m3u8

exit 0
