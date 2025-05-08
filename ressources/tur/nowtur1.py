import requests
import re

url = 'http://www.nowtv.com.tr/canli-yayin'  # changed to HTTP

try:
    response = requests.get(url, timeout=10)  # removed verify=False (not needed for HTTP)

    if response.status_code == 200:
        match = re.search(r"daiUrl\s*:\s*'(https?://[^\']+)'", response.text)

        if match:
            erstrm = match.group(1)
            print(erstrm)
        else:
            print("erstrm not found in the content.")
    else:
        print(f"Failed to fetch content. HTTP Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
