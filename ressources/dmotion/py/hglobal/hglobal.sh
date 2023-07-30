#!/bin/bash
# Thanks to LITUATUI user on github
cd ressources/dmotion/py/hglobal

python hglobal.py && sed -e '/x81x3cd/ {' -e 'r hglobal.txt' -e 'd' -e '}' -i hglobal.m3u8

exit 0
