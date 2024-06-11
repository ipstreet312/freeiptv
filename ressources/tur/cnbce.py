import streamlink
streams = streamlink.streams('https://www.cnbce.com/canli-yayin')
master = streams["best"].multivariant.uri
print(master)
