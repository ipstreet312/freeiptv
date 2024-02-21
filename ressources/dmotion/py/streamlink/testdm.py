import streamlink
import requests
streams = streamlink.streams('https://www.dailymotion.com/video/x5gv5v0')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
