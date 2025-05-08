import requests
import socket
import re
from requests.packages.urllib3.util import connection

# Patch urllib3 to use only IPv4
def force_ipv4_dns(host, port=0, family=socket.AF_INET, type=0, proto=0, flags=0):
    return socket.getaddrinfo(host, port, socket.AF_INET, type, proto, flags)

connection.orig_getaddrinfo = socket.getaddrinfo
socket.getaddrinfo = force_ipv4_dns

url = 'http://www.nowtv.com.tr/canli-yayin'  # Using HTTP instead of HTTPS

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        match = re.search(r"daiUrl\s*:\s*'(https?://[^\']+)'", response.text)
        if match:
            erstrm = match.group(1)
            print(erstrm)
        else:
            print("erstrm not found in the content.")
    else:
        print(f"Failed to fetch content. HTTP Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
finally:
    # Restore original DNS resolution
    socket.getaddrinfo = connection.orig_getaddrinfo
