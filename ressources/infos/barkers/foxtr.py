import requests
import re
from bs4 import BeautifulSoup

def extract_src_from_html(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    script_tags = soup.find_all('script')

    daion_url = None
    for tag in script_tags:
        if "daionUrl" in tag.text:
            match = re.search(r"daionUrl\s*:\s*'([^']*)'", tag.text)
            if match:
                daion_url = match.group(1)
                break

    return daion_url

def fetch_html_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def main():
    # URL to fetch HTML content
    url = 'https://www.fox.com.tr/canli-yayin'

    # Fetch HTML content
    html_code = fetch_html_content(url)
    
    if html_code:
        src = extract_src_from_html(html_code)
        if src:
            src = src.strip("'\"")
            print(src)
        else:
            print("No 'daionUrl' found in the HTML content.")
    else:
        print("Failed to fetch HTML content from the URL.")

if __name__ == "__main__":
    main()
