import streamlink
import requests
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
master2 = streams["best"].url
content2 = requests.get(master2)
print(content2.text)
