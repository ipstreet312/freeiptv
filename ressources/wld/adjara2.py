import requests

url = "https://tv.canlitvvolo.com/Tv/TVShow"
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://tv.canlitvvolo.com",
    "Referer": "https://tv.canlitvvolo.com",
    "User-Agent": "Mozilla/5.0",
}
data = {
    "channelSeoName": "adjara-tv"  # <-- replace with actual payload fields
}
response = requests.post(url, json=data, headers=headers)
print(response.json())
