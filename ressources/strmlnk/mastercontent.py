import streamlink
import requests
streams = streamlink.streams('https://stream.tvp.pl/?channel_id=1455')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
