import streamlink
import requests
headers = {
    "visitorCountry": "FR"
}
streams = streamlink.streams('https://media.gov.kw/LiveTV.aspx?PanChannel=KTV1', headers=headers)
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
