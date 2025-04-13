import streamlink
session = streamlink.session.Streamlink(options={"ipv4": True})
streams = session.streams('https://stream.tvp.pl/?channel_id=1455')
dastrm = streams["best"].multivariant.uri
print(dastrm)
