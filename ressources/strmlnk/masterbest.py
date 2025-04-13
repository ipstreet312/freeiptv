import streamlink
streams = streamlink.streams('https://stream.tvp.pl/?channel_id=1455')
erstrm = streams["best"].multivariant.uri
print(erstrm)
