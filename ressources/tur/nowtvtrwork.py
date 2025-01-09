import streamlink
session = streamlink.session.Streamlink(options={"ipv4": True})
streams = session.streams('https://www.nowtv.com.tr/canli-yayin')
dastrm = streams["best"].multivariant.uri
print(dastrm)
