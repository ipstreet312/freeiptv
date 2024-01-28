import re
import requests
from bs4 import BeautifulSoup

url = "https://www.fox.com.tr/canli-yayin"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

script_tag = soup.find('script', {'type': 'text/javascript'})
print("Script Content:", script_tag.text)

url_match = re.search(r"daiUrl\s*:\s*'([^']+)'", script_tag.text, re.DOTALL)
if url_match:
    dai_url = url_match.group(1)
    print("Retrieved URL:", dai_url)
else:
    print("URL not found in the script.")
