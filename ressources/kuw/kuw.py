import streamlink
import requests
session = streamlink.session.Streamlink(options={"ipv4": True})
streams = session.streams('http://media.gov.kw/LiveTV.aspx?PanChannel=KTV1')
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
