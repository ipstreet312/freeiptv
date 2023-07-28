#!/bin/bash

sed -i "/lci-cmaf/ c  $(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/btv/py/lci.m3u8 -o /dev/null -O -)" all.m3u

exit 0
