import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
dastrm = streams["best"].multivariant.uri
print(dastrm)
