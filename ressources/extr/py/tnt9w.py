import requests
from bs4 import BeautifulSoup
import re

url = "https://www.tntendirect.com/W9-en-direct"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
scripts = soup.find_all('script')

for script in scripts:
    match = re.search(r'source:\s*"(.*?\.m3u8\?wmsAuthSign=.*?)",', script.text)
    if match:
        m3u8_link = match.group(1)
        print("Found .m3u8 link:", m3u8_link)
        break
else:
    print("No .m3u8 link found.")
