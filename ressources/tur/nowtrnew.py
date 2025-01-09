import streamlink
session = streamlink.Streamlink()
session.set_option("http-no-ssl-verify", True)
streams = session.streams('https://www.nowtv.com.tr/canli-yayin')
dastrm = streams["best"].url
print(dastrm)
