#!/bin/bash

cd feed

python atvtr.py && sed -e '/atv/ {' -e 'r atvtr.txt' -e 'd' -e '}' -i atvtr.m3u8

exit 0
