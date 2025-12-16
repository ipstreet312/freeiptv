import requests
import re
import json
import urllib3

base_url = "https://ciner-live.ercdn.net/showturk/"

urllib3.disable_warnings()

response = requests.get(
    "https://www.showturk.com.tr/canli-yayin",
    verify=False,
    timeout=15
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
                content_response = requests.get(ht_stream_m3u8)

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
    print("Error: Status code is not 200.")
