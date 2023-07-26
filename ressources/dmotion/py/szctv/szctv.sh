#!/bin/bash
# Thanks to pshanmu3 user on github
echo $(dirname $0)
cd $(dirname $0)
python3 szctv.py > ../ressources/dmotion/py/szctv/szctv.m3u8

echo m3u grabbed