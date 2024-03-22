import streamlink
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp2')
master4 = streams["best"].url
print(master4)
