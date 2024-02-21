import streamlink
import requests
streams = streamlink.streams('https://www.dailymotion.com/video/k2IuM11CZakq4ZvrUkv')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
