import streamlink
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin', HLSStream["best"][1])
print(streams)
