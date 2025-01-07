import streamlink
import requests
streams = streamlink.streams('https://player.vimeo.com/video/1044527541')
print(streams)
