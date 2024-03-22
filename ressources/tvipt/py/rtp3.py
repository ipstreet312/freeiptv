import streamlink
import requests
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp3')
master3 = streams["best"].url
content3 = requests.get(master3)
print(content3.text)
