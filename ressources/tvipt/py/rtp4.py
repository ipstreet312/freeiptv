import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
master4 = streams["best"].url
print(master4)
