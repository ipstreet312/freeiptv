import streamlink
session = streamlink.session.Streamlink(options={"ipv4": True})
streams = session.streams('https://www.nowtv.com.tr/canli-yayin')
erstrm = streams["best"].multivariant.uri
print(erstrm)
