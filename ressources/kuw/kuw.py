import streamlink
import requests
streams = streamlink.streams('https://player.mangomolo.com/v1/live?id=MTk1&channelid=MzU1&countries=bnVsbA==&w=100%25&h=100%25')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
