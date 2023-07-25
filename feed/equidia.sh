#!/bin/bash

echo $(dirname $0)
cd $(dirname $0)
python3 equidia.py > ../feed/equidia.m3u8

echo m3u grabbed
