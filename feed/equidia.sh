#!/bin/bash
echo $(dirname $0)
cd feed
python3 equidia.py > ../feed/equidia.m3u8

echo m3u grabbed
