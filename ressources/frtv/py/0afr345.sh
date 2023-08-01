#!/bin/bash

sed -i "/France_3/hls_fr3/ c  $(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/frtv/py/0fr3.m3u8 -o /dev/null -O -)" all.m3u

sed -i "/France_4/hls_fr4/ c  $(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/frtv/py/0fr4.m3u8 -o /dev/null -O -)" all.m3u

sed -i "/France_5/hls_fr5/ c  $(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/frtv/py/0fr5.m3u8 -o /dev/null -O -)" all.m3u

exit 0
