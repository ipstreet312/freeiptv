import requests
import re

url = 'https://www.nowtv.com.tr/canli-yayin'

response = requests.get(url, verify=False)

if response.status_code == 200:
    match = re.search(r"daiUrl\s*:\s*'(https?://[^\']+)'", response.text)
  
    if match:
        dai_url = match.group(1)
        print(f"The extracted daiUrl is: {dai_url}")
    else:
        print("daiUrl not found in the content.")
else:
    print(f"Failed to fetch content. HTTP Status code: {response.status_code}")
