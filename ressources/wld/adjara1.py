import requests

url = "https://tv.canlitvvolo.com/Tv/TVShow"
headers = {
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://tv.canlitvvolo.com",
    "Referer": "https://tv.canlitvvolo.com",
    "User-Agent": "Mozilla/5.0"
}
payload = {
    # Use the same JSON as the request body from DevTools
    # Example:
    "channel": "Adjara TV"
}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
