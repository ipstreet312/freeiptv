import streamlink
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin')
print(streams["best"].multivariant.uri)
