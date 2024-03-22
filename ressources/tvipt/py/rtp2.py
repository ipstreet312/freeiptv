import streamlink
import requests
streams = streamlink.streams('https://www.rtp.pt/play/direto/rtp2')
master2 = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master2)
content2 = response.text
print(content2)
