import streamlink
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin')
master_stream = streams['best'][1]
master_url = master_stream.url
print(master_url)
