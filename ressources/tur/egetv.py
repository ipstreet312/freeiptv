import requests

url = "https://cdnet.alwaysdata.net/egetvcurl.php?m3u8"

response = requests.get(url)

if response.status_code == 200:
    content = response.text
    print(content)
else:
    print(f"Failed to retrieve the file. Status code: {response.status_code}")
