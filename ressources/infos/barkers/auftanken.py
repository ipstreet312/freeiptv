import requests
from bs4 import BeautifulSoup

def extract_src_from_html(html_code):
    soup = BeautifulSoup(html_code, 'html.parser')
    script_tag = soup.find('script', string=lambda text: text and 'player.source =' in text)
    src_value = None
    if script_tag:
        src_start = script_tag.string.find("'https://")  
        src_end = script_tag.string.find(".m3u8'") + len(".m3u8'")
        src_value = script_tag.string[src_start:src_end]
    return src_value

def main():
    # Fetch HTML content from the URL
    url = 'https://webplayer.sbctv.ch/auftanken/'
    response = requests.get(url)
    
    if response.status_code == 200:
        html_code = response.text
        src = extract_src_from_html(html_code)
        if src:
            src = src.strip("'\"")
            print(src)
        else:
            print("No 'player.source =' found in the HTML content.")
    else:
        print("Failed to fetch HTML content. Status code:", response.status_code)

if __name__ == "__main__":
    main()
