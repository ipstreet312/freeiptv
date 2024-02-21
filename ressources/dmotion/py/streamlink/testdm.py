import streamlink
import requests
streams = streamlink.streams('https://www.dailymotion.com/video/x21oo10')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
