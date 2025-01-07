import streamlink
import requests
streams = streamlink.streams('https://player.vimeo.com/video/1044527541')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
