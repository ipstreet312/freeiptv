import streamlink
session = streamlink.Streamlink
streams = session.streams('https://www.nowtv.com.tr/canli-yayin')
erstrm = streams["best"].multivariant.uri
print(erstrm)
