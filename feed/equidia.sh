#!/bin/bash
# Thanks to pshanmu3 user on github
echo $(dirname $0)
cd $(dirname $0)
python3 equidia.py http://62.210.135.99:80 > equidia.m3u8

echo m3u grabbed
