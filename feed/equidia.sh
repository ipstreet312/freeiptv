#!/bin/bash
cd /home/runner/work/freeiptv/feed
python3 equidia.py http://62.210.135.99:80 > ./feed/equidia.m3u8

echo m3u grabbed
