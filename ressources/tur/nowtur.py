import requests
from bs4 import BeautifulSoup
import re
import urllib3

url = "http://www.nowtv.com.tr/canli-yayin"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

try:
    response = requests.get(url, verify=False)
    response.raise_for_status()
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")
    script_tag = soup.find('script', text=True)

    if script_tag:
        script_content = script_tag.string
        match = re.search(r"daiUrl\s*:\s*'(https?://[^']+)'", script_content)
        if match:
            daiUrl = match.group(1)
            print("Extracted daiUrl:", daiUrl)
        else:
            print("daiUrl not found.")
    else:
        print("No <script> tag with the required content found.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred while fetching the URL: {e}")
