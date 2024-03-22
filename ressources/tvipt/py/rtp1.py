import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
master1 = streams["best"].multivariant.uri
print(master1)
