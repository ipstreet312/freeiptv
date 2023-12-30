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

def main():
    # Fetch HTML content from the URL
    url = 'https://www.fox.com.tr/canli-yayin'
    response = requests.get(url)
    
    if response.status_code == 200:
        html_code = response.text
        src = extract_src_from_html(html_code)
        if src:
            src = src.strip("'\"")
            print(src)
        else:
            print("No 'daionUrl' found in the HTML content.")
    else:
        print("Failed to fetch HTML content. Status code:", response.status_code)

if __name__ == "__main__":
    main()
