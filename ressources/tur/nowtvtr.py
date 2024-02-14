import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin', ipv4=True)
erstrm = streams["best"].multivariant.uri
print(erstrm)
