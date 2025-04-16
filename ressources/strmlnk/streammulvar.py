import streamlink
streams = streamlink.streams('https://stream.tvp.pl/?channel_id=1455')
beststrmmul = streams["best"].multivariant.uri
print(beststrmmul)
print("XXX")
hlsmultimul = streams["hls-multi"].multivariant.uri
print(hlsmultimul)
print("XXX")
dashlmul = streams["dash"].multivariant.uri
print(dashlmul)
