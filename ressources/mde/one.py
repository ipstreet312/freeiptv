import requests
from bs4 import BeautifulSoup

url = 'https://media.mtv.com.lb/live/one'

response = requests.get(url)
webpage_content = response.content

soup = BeautifulSoup(webpage_content, 'html.parser')

source_tag = soup.find('source', {'type': 'application/x-mpegURL'})

if source_tag:
    m3u8_link = source_tag.get('src')
    print(m3u8_link)
else:
    print("No m3u8 link found.")
