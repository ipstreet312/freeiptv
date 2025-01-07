import requests

# The initial URL
url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

# Make a GET request with allow_redirects=True (default behavior)
response = requests.get(url, allow_redirects=True)

# Print the original URL and the final redirected URL
print("Original URL:", url)
print("Final URL after redirection:", response.url)
