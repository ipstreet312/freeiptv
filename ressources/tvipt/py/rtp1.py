import streamlink
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp1')
rtp1 = streams["best"].multivariant.uri
print(rtp1)
