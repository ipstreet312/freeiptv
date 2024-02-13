from streamlink.plugins.foxtr import streams
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
print(streams["best"].multivariant.uri)
