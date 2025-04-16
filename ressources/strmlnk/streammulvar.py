import streamlink
streams = streamlink.streams('https://stream.tvp.pl/?channel_id=1455')
beststrmmul = streams["best"].multivariant.uri
print(beststrmmul)
print("XXX")
dashlmul = streams["dash"].multivariant.uri
print(dashlmul)
