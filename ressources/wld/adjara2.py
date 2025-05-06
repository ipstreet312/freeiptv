import requests

# Endpoint that returns the token
url = "https://tv.canlitvvolo.com/Tv/TVShow"

# Request headers (mimic browser as closely as needed)
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://tv.canlitvvolo.com",
    "Referer": "https://tv.canlitvvolo.com",
    "User-Agent": "Mozilla/5.0"
}

# Payload based on browser request
payload = {
    "permalink": "adjara-tv-canli/",
    "yayin": 1
}

# Send the POST request
response = requests.post(url, json=payload, headers=headers)
data = response.json()

# Display the m3u8 URL (usually inside a nested structure)
print(data)

# Optional: extract direct stream URL
try:
    stream_url = data['data']['playerUrl']
    print("Stream URL:", stream_url)
except KeyError:
    print("Token or stream URL not found in response.")
