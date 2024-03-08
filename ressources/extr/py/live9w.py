from bs4 import BeautifulSoup
import requests

url = 'https://www.livehdtv.net/token.php?stream=w9'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
script_tag = soup.find('script')

script_content = script_tag.contents[0]
script_lines = script_content.split('\n')

m3u8_link = None
for line in script_lines:
    if 'file:' in line:
        m3u8_link = line.split('"')[1]
        break

print("Extracted .m3u8 link:", m3u8_link)
