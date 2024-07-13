import streamlink
import requests
streams = streamlink.streams('https://www.aloula.sa/en/live/saudiatv')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
