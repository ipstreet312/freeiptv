import streamlink
session = streamlink.session.Streamlink(options={"http-no-ssl-verify": True})
streams = session.streams('https://www.nowtv.com.tr/canli-yayin')
dastrm = streams["best"].multivariant.uri
print(dastrm)
