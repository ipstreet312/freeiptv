import requests
import re
import json
import certifi

base_url = "https://ciner-live.ercdn.net/showturk/"
url = "https://www.showturk.com.tr/canli-yayin"

# ✅ Headers to avoid bot blocking / broken TLS chains
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection": "keep-alive",
}

# ✅ Explicit CA bundle (fixes SSL error)
response = requests.get(
    url,
    headers=headers,
    timeout=15,
    verify=certifi.where()
)

if response.status_code == 200:
    site_content = response.text

    match = re.search(r"data-hope-video='(.*?)'", site_content, re.DOTALL)

    if match:
        json_data_raw = match.group(1)
        json_data_valid = json_data_raw.replace("\\/", "/")

        try:
            ht_data = json.loads(json_data_valid)

            m3u8_list = ht_data.get('media', {}).get('m3u8', [])
            ht_stream_m3u8 = m3u8_list[0].get('src') if m3u8_list else None

            if ht_stream_m3u8:
                # ✅ Same headers + cert for the m3u8 request
                content_response = requests.get(
                    ht_stream_m3u8,
                    headers=headers,
                    timeout=15,
                    verify=certifi.where()
                )

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
                    print("Error fetching content from the Live URL.")
            else:
                print("Live URL not found in the JSON data.")

        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")

    else:
        print("data-hope-video JSON not found in the content.")

else:
    print(f"Error: Status code is {response.status_code}")
