import requests

github_url = "https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/nrj/nrj12.m3u8"
base_url = "https://event1.nrjaudio.fm/hls/live/2038378/nrj_12/"

def fetch_m3u8_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Ensure bad responses if any
    lines = response.text.splitlines()
    
    # Construct full URLs
    updated_lines = []
    for line in lines:
        if line.startswith("hdntl="):
            updated_lines.append(base_url + line)
        else:
            updated_lines.append(line)
    
    return "\n".join(updated_lines)

if __name__ == "__main__":
    try:
        content = fetch_m3u8_content(github_url)
        print(content)
    except Exception as e:
        print(f"An error occurred: {e}")
