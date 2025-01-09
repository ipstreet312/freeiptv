import streamlink
session = streamlink.Streamlink(
    options={
        "http-no-ssl-verify": True,
        "no-check-certificate" : True,
        "http-disable-dh": True,
        "ipv4": True
    }
)
streams = session.streams('http://www.nowtv.com.tr/canli-yayin')
dastrm = streams["best"].multivariant.uri
print(dastrm)
