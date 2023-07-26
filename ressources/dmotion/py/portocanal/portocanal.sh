#!/bin/bash
# Thanks to LITUATUI user on github
cd ressources/dmotion/py/portocanal

python portocanal.py && sed -e '/x8egnb8/ {' -e 'r portocanal.txt' -e 'd' -e '}' -i portocanal.m3u8

exit 0