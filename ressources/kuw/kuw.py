import streamlink
import requests
streams = streamlink.streams('https://www.media.gov.kw/LiveTV.aspx?PanChannel=KTV1')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
