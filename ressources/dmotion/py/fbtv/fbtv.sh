#!/bin/bash
# Thanks to pshanmu3 user on github
echo $(dirname $0)
cd $(dirname $0)
python3 fbtv.py > ../ressources/dmotion/py/fbtv/fbtv.m3u8

echo m3u grabbed