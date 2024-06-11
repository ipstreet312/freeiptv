import streamlink
streams = streamlink.streams('https://www.cnbce.com/canli-yayin')
master = streams["best"].[0]
print(master)
