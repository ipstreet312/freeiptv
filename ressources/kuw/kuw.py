import streamlink
import requests
headers = {
    "visitorCountry": "FR"
}
response = requests.get('https://media.gov.kw/LiveTV.aspx?PanChannel=KTV1', headers=headers)
streams = streamlink.streams('https://media.gov.kw/LiveTV.aspx?PanChannel=KTV1', response_content=response.content)
master = streams["best"].multivariant.uri
s = requests.Session()
response = s.get(master)
content = response.text
print(content)
