#!/bin/bash

erstrm_content=$(curl -s "${erstrm}")
dastrm_content=$(curl -s "${dastrm}")

sed -i "s|https://nowtv-live-ad.ercdn.net.*|${erstrm_content}|g" test.m3u
sed -i "s|https://nowtv.daioncdn.net.*|${dastrm_content}|g" test.m3u
