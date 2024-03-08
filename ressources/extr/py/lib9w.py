import requests
from bs4 import BeautifulSoup

# URL of the web page
url = "http://callofliberty.fr/tv/22-6ter/22-6ter.php"

# Fetch the HTML content from the URL
response = requests.get(url)
html_content = response.text

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the script tag containing the player configuration
script_tag = soup.find('script')

# Extract the source URL from the script tag
source_url = None
if script_tag:
    source_url = script_tag.string.split("source: '")[1].split("'")[0]

print(source_url)
