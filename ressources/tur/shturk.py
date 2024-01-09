import requests
import re
import json

base_url = "https://ciner-live.ercdn.net/showturk/"
url = "https://www.showturk.com.tr/canli-yayin/showturk"
response = requests.get(url)

if response.status_code == 200:
    site_content = response.text
    match = re.search(r'ht_stream_m3u8":"(.*?)"', site_content)
    
    if match:
        json_data = match.group(1)
        json_data_valid = json_data.replace("'", '"')
        #print(f"Extracted JSON data: {json_data_valid}")
        content_response = requests.get(json_data_valid)
        
        if content_response.status_code == 200:
            content = content_response.text
            lines = content.split("\n")
            modified_content = ""
            
            for line in lines:
                if line.startswith("showturk"):
                    full_url = base_url + line
                    modified_content += full_url + "\n"
                else:
                    modified_content += line + "\n"
            
            print(modified_content)
        else:
            print("Live URL not found in the content.")
    else:
        print("Live URL pattern not found in the content.")
else:
    print("Error: Status code is not 200.")
