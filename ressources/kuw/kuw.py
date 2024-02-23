import streamlink
import requests
streams = streamlink.streams('https://player.mangomolo.com/v1/live?id=MTk1&channelid=MzU1&countries=bnVsbA==&w=100%25&h=100%25&&autoplay=true&filter=none&signature=9ea6c8ed03b8de6e339d6df2b0685f25&app_id=43')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
