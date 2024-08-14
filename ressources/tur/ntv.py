import requests
import re

base_url = "https://mn-nl.mncdn.com/dogusdyg_ntv/dogusdyg_ntv.smil/"
url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"
response = requests.get(url)

response_url = response.text.strip()
modified_url = response_url.replace("kralpoptv", "ntv")

content_response = requests.get(modified_url)
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
