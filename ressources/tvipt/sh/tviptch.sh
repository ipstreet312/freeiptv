#!/bin/bash
files=(
  "ressources/tvipt/sh/cnnpt.m3u8"
  "ressources/tvipt/sh/tvi.m3u8"
  "ressources/tvipt/sh/tviint.m3u8"
)
for file in "${files[@]}"; do
  sed -i "s#wmsAuthSign=[^&]*#wmsAuthSign=$(wget -qO- https://services.iol.pt/matrix?userId -o /dev/null)#g" "$file"
done
exit 0
