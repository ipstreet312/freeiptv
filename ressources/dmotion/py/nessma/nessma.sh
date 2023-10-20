#!/bin/bash
# Thanks to LITUATUI user on github
cd ressources/dmotion/py/nessma

python nessma.py && sed -e '/x7va0xb/ {' -e 'r nessma.txt' -e 'd' -e '}' -i nessma.m3u8

exit 0
