#!/bin/bash

sed -i "/lci-cmaf/ c  $(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/equid/py/equid1.m3u8 -o /dev/null -O -)" all.m3u

exit 0
