from streamlink.plugins.foxtr import FoxTR
streams = FoxTR.streams('https://www.nowtv.com.tr/canli-yayin')
print(streams["best"].multivariant.uri)
