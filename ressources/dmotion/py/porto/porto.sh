#!/bin/bash
# Thanks to LITUATUI user on github
cd ressources/dmotion/py/porto

python porto.py && sed -e '/x8egnb8/ {' -e 'r porto.txt' -e 'd' -e '}' -i porto.m3u8

exit 0
