import requests

url = "https://uzunmuhalefet.serv00.net/canlitv2.php?id=841&.m3u8"
base_url = "http://50.7.218.154:1935/canlitv/egetv.stream/"

response = requests.get(url)

if response.status_code == 200:
    content = response.text
    modified_content = content.replace("chunklist", base_url + "chunklist")
    print(modified_content)
else:
    print(f"Failed to retrieve the file. Status code: {response.status_code}")
