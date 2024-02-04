import streamlink
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin')
master_url = streams['best'][0]
print(master_url)
