#!/bin/bash

erstrm_content=$(curl -s "$1")
dastrm_content=$(curl -s "$2")

sed -i "s|https://nowtv-live-ad.ercdn.net.*|${erstrm_content}|g" ressources/tur/test.m3u
sed -i "s|https://nowtv.daioncdn.net.*|${dastrm_content}|g" ressources/tur/test.m3u
