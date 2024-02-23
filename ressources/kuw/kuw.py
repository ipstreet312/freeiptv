import streamlink
import requests
streams = streamlink.streams('https://player.mangomolo.com/v1/live?id=MTk1&channelid=MzU2&countries=bnVsbA==&w=100%25&h=100%25&autoplay=true&filter=none&signature=6dbebfb531d4dfb9a798f6309ea9260c&app_id=43')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
