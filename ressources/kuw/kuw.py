import streamlink
import requests
url = 'https://player.mangomolo.com/v1/live?id=MTk1&channelid=MzU1&countries=bnVsbA==&w=100%25&h=100%25&autoplay=true&filter=none&signature=9ea6c8ed03b8de6e339d6df2b0685f25&app_id=43'
streams = streamlink.streams(url)
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
