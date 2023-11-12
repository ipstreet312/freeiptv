#!/bin/bash
sed "s#wmsAuthSign=[^&]*#wmsAuthSign=$(wget -qO- https://services.iol.pt/matrix?userId -o /dev/null)#g" ressources/tvipt/sh/cnnpt.m3u8
exit 0
