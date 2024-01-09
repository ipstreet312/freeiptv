import requests
import re

url = "https://www.eurostartv.com.tr/canli-izle"
response = requests.get(url)

if response.status_code == 200:
    site_content = response.text
    match = re.search(r'liveUrl = \'(.*?)\'', site_content)
    
    if match:
        baglanti = match.group(1)
        #print(f"Location: {baglanti}")
         content_response = requests.get(baglanti)
         if content_response.status_code == 200:
             content = content_response.text
             print(content)
    else:
        print("Live URL not found in the content.")
else:
    print("Failed to fetch the website content.")
