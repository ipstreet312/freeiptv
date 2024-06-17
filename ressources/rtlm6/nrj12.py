import requests

github_url = "https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/nrj/nrj12.m3u8"
base_url = "https://event1.nrjaudio.fm/hls/live/2038378/nrj_12/"

headers = {
    'User-Agent': 'SmartOs Tv'
}

def fetch_m3u8_content(url):
    response = requests.get(url, headers=headers)  # Include headers here
    response.raise_for_status()  # Ensure we notice bad responses
    lines = response.text.splitlines()

    # Fetch the content of the third link
    if len(lines) > 2:
        third_link = lines[2]
        third_response = requests.get(third_link, headers=headers)  # Include headers here
        third_response.raise_for_status()
        third_content = third_response.text.splitlines()
        
        # Construct full URLs
        updated_lines = []
        for line in third_content:
            if line.startswith("hdntl="):
                updated_lines.append(base_url + line)
            else:
                updated_lines.append(line)
        
        return "\n".join(updated_lines)
    else:
        raise ValueError("The file does not contain enough links.")

if __name__ == "__main__":
    try:
        content = fetch_m3u8_content(github_url)
        print(content)
    except Exception as e:
        print(f"An error occurred: {e}")
