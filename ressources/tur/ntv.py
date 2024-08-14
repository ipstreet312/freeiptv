import requests

base_url = "https://mn-nl.mncdn.com/dogusdyg_ntv/dogusdyg_ntv.smil/"
initial_url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

try:
    response = requests.get(initial_url)
    response.raise_for_status()

    final_url = response.url
    modified_url = final_url.replace("kralpoptv", "ntv")

    content_response = requests.get(modified_url)
    content_response.raise_for_status()
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

except requests.RequestException as e:
    print(f"An error occurred: {e}")
