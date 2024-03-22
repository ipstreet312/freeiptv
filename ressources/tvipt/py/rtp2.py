import streamlink
import requests
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp2')
master2 = streams["best"].url
content2 = requests.get(master2)
print(content2.text)
