from streamlink.plugins.foxtr import foxtr
streams = foxtr.streams('https://www.nowtv.com.tr/canli-yayin')
print(streams["best"].multivariant.uri)
