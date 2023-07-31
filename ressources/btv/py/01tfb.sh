#!/bin/bash

content=$(wget https://raw.githubusercontent.com/ipstreet312/freeiptv/master/ressources/btv/py/01tf.m3u8 -o /dev/null -O -)
updated_content="${content}.m3u8"

sed -i "/tf1-cmaf/ c ${updated_content}" all.m3u

exit 0
