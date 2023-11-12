#!/bin/bash

file1="ressources/tvipt/sh/cnnpt.m3u8"
file2="ressources/tvipt/sh/tvi.m3u8"
file3="ressources/tvipt/sh/tviint.m3u8"

for file in "$file1" "$file2" "$file3"; do
  sed -i "s#wmsAuthSign=[^&]*#wmsAuthSign=$(wget -qO- https://services.iol.pt/matrix?userId -o /dev/null)#g" "$file"
done
exit 0
