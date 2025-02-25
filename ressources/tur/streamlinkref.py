import streamlink
streams = streamlink.streams('https://www.atresplayer.com/directos/antena3-internacional/')
strmlnk = streams["best"].multivariant.uri
print(strmlnk)
