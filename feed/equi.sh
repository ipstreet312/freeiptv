#!/bin/bash
echo $(dirname $0)
cd $(dirname $0)
python3 equi.py > ../feed/equi.m3u8

echo m3u grabbed