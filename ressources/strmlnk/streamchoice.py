import streamlink
streams = streamlink.streams('https://stream.tvp.pl/?channel_id=1455')
beststrm = streams["best"]
print(beststrm)
print("XXX")
hlsmulti = streams["hls-multi"]
print(hlsmulti)
print("XXX")
dashl = streams["dash"]
print(dashl)
