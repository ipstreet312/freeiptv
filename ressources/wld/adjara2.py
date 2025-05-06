import requests

url = "https://tv.canlitvvolo.com/Tv/TVShow"

headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://tv.canlitvvolo.com",
    "Referer": "https://tv.canlitvvolo.com/adjara-tv-canli/?yayin=1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*"
}

payload = {
    "permalink": "adjara-tv-canli/",
    "yayin": 1,
    "ip": "111.222.222.111",       # optional, spoofed IP
    "ipcountry": "PR",             # optional, spoofed country
    "mobile": 1
}

response = requests.post(url, json=payload, headers=headers)

# Debug output
print("Status Code:", response.status_code)

if response.status_code != 200:
    print("Error: Unexpected response code")
    print("Response body:", response.text)
    exit(1)

try:
    data = response.json()
    stream_url = data['data']['playerUrl']
    # Output an .m3u8 playlist format
    print("#EXTM3U")
    print("#EXTINF:-1,Adjara TV")
    print(stream_url)
except Exception as e:
    print("Failed to parse JSON:", e)
    print("Raw response text:", response.text)
