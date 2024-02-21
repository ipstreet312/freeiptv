import streamlink
import requests
streams = streamlink.streams('https://www.dailymotion.com/video/x7va0xb')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
