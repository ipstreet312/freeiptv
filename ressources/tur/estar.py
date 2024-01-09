import requests
import re

base_url = "http://mn-nl.mncdn.com/dogusdyg_eurostar/dogusdyg_eurostar.smil/"
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
            lines = content.split("\n")
            modified_content = ""
            
            for line in lines:
                if line.startswith("chunklist"):
                    full_url = base_url + line
                    modified_content += full_url + "\n"
                else:
                    modified_content += line + "\n"
            
            print(modified_content)
        else:
            print("Failed to fetch content.")
    else:
        print("Live URL not found in the content.")
else:
    print("Failed to fetch the website content.")
