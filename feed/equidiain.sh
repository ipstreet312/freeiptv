#!/bin/bash

sed -i "/eqdlivepri_fre.smil/ c  $(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/feed/equidia.m3u8 -o /dev/null -O -)" all.m3u

exit 0
