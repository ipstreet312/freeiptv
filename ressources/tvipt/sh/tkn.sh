#!/bin/bash
sed 's/wmsAuthSign=/&(wget https://services.iol.pt/matrix?userId -o /dev/null -O -)/g' ressources/tvipt/sh/cnnpt.m3u8
exit 0
