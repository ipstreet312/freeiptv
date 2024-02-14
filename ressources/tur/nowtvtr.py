import streamlink
streamlink.set_option("ipv4", True)
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
erstrm = streams["best"].multivariant.uri
print(erstrm)
