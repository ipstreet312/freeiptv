import streamlink
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp1')
master1 = streams["best"].multivariant.uri
print(master1)
