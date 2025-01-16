import streamlink
session = streamlink.Streamlink(options={"ipv4": True})
streams = session.streams('http://www.nowtv.com.tr/canli-yayin')
erstrm = streams["best"].multivariant.uri
print(erstrm)
