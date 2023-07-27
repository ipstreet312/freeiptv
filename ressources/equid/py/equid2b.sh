#!/bin/bash

sed -i "/equidia-website-web-1/ c  $(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/equid/py/equid2.m3u8 -o /dev/null -O -)" all.m3u

exit 0
