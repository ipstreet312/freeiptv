import streamlink
session = streamlink.Streamlink(
    options={
        "http-no-ssl-verify": True,
        "no-check-certificate" : True,
        "http-disable-dh": True,
        "ipv4": True
    }
)
streams = session.streams('https://stream.tvp.pl/?channel_id=1455')
dastrm = streams["best"].multivariant.uri
print(dastrm)
