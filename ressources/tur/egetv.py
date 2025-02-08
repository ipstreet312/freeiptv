import requests

url = "https://egetest"

response = requests.get(url)

if response.status_code == 200:
    content = response.text
    lines = content.splitlines()
    for line in lines:
        print(line)
else:
    print(f"Failed to retrieve the file. Status code: {response.status_code}")
