import streamlink
session = streamlink.session.Streamlink(options={"no-check-certificate": True})
streams = session.streams('https://www.nowtv.com.tr/canli-yayin')
dastrm = streams["best"].multivariant.uri
print(dastrm)
