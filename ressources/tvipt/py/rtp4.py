import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
master1 = streams["best"].url
print(master1)
