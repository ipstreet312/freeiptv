import requests
from bs4 import BeautifulSoup

def get_kwik_key_from_page():
    url = "https://rotana.net/en/channels"
    headers = {
        'Referer': 'https://rotana.net/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'Content-Type': 'application/x-mpegURL',
        'Origin': 'https://rotana.net',
        'X-Forwarded-For': '216.239.80.141'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    target_channel_id = "rotana-lbc"
    channel_div = soup.find("a", {"id": target_channel_id})
    
    if channel_div:
        kwik_key = channel_div.get('onclick').split("'")[-2]
        return kwik_key
    else:
        print("Channel ID not found on the page")
        return None

def get_channel_token(kwik_key, media_url):
    url = "https://rotana.net/channels/generateAclToken"
    data = {
        'kwik_key': kwik_key,
        'mediaUrl': media_url
    }
    headers = {
        'Referer': 'https://rotana.net/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://rotana.net',
        'X-Forwarded-For': '216.239.80.141'
    }
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    
    try:
        response_json = response.json()
        return response_json['data']
    except ValueError:
        print("Failed to parse JSON response")
        return None

def construct_m3u8_link(media_url, acl_token):
    return f"https://live.kwikmotion.com/{media_url}live/{media_url}.smil/playlist.m3u8?hdnts={acl_token}"

kwik_key = get_kwik_key_from_page()
media_url = "rlbc"
media_id = "rotanalbc"

if kwik_key:
    acl_token = get_channel_token(kwik_key, media_url)
    if acl_token:
        m3u8_link = construct_m3u8_link(media_url, acl_token)
        response = requests.get(m3u8_link)
        print(response.text)
        print(m3u8_link)
    else:
        print("Failed to retrieve ACL token")
else:
    print("Failed to retrieve kwik_key from the page")
