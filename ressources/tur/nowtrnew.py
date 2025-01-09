import streamlink
session = streamlink.Streamlink(
    options={
        "http-no-ssl-verify": True,
        "http-disable-dh": True
    }
)
streams = session.streams('http://www.nowtv.com.tr/canli-yayin')
dastrm = streams["best"].multivariant.uri
print(dastrm)
