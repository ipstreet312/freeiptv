#!/bin/bash

echo $(dirname $0)

python3 -m pip install requests

cd $(dirname $0)/ressources/ytbe

python3 atvtr.py > ../atvtr.m3u8

echo m3u8 grabbed
