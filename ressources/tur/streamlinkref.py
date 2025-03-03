import streamlink
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtpmadeira')
strmlnk = streams["best"].multivariant.uri
print(strmlnk)
