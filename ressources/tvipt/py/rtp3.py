import streamlink
import requests
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp1')
master3 = streams["best"].multivariant.uri
content3 = requests.get(master3)
print(content3.text)
