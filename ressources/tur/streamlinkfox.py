import streamlink
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin', M3U8)
print(streams)
