import ssl
import urllib.request
import re

# Create an SSL context to disable certificate verification
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# URL to fetch
url = 'https://www.nowtv.com.tr/canli-yayin'

try:
    # Fetch the HTML content
    with urllib.request.urlopen(url, context=ssl_context) as response:
        html_content = response.read().decode('utf-8')

    # Search for daiUrl using regex
    match = re.search(r"daiUrl\s*:\s*'([^']+)'", html_content)

    if match:
        print(match.group(1))
    else:
        print("daiUrl not found in the content.")
except Exception as e:
    print(f"An error occurred: {e}")
