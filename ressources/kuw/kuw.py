import streamlink
import requests
streams = streamlink.streams('mangomolo')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
