import streamlink
import requests
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp3')
master3 = streams["best"].url
s = requests.Session()
response = s.get(master3)
content3 = response.text
print(content3)
