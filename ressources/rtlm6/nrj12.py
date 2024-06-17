import requests

github_url = "https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/nrj/nrj12.m3u8"

def fetch_m3u8_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure bad responses if any
    lines = response.text.splitlines()
    
    # Fetch the content of the third link
    if len(lines) > 2:
        third_link = lines[2]
        third_response = requests.get(third_link)
        third_response.raise_for_status()
        return third_response.text
    else:
        raise ValueError("The file does not contain enough links.")

if __name__ == "__main__":
    try:
        content = fetch_m3u8_content(github_url)
        print(content)
    except Exception as e:
        print(f"An error occurred: {e}")
