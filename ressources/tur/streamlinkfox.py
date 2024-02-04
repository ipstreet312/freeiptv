import streamlink
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin', multivariant)
print(streams)
