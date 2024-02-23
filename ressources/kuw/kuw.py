import streamlink
import requests
streams = streamlink.streams('https://media.gov.kw/LiveTV.aspx?PanChannel=KTV2')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
