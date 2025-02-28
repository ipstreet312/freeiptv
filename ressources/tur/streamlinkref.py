import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
strmlnk = streams["best"].multivariant.uri
print(strmlnk)
