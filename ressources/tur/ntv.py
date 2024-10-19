import requests

def fetch_and_save_to_file(base_url, variant, output_file):
    initial_url = f"https://dygvideo.dygdigital.com/live/hls/{variant}?m3u8"

    try:
        response = requests.get(initial_url)
        response.raise_for_status()

        final_url = response.url
        modified_url = final_url.replace(f"dogusdyg_{variant}/dogusdyg_{variant}.smil/playlist", f"dogusdyg_{base_url}/live")

        content_response = requests.get(modified_url)
        content_response.raise_for_status()
        content = content_response.text
        
        save_to_file(content, base_url, output_file)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def save_to_file(content, base_url, output_file):
    lines = content.split("\n")
    modified_content = ""

    for line in lines:
        if line.startswith("live_"):
            full_url = f"https://mn-nl.mncdn.com/dogusdyg_{base_url}/" + line
            modified_content += full_url + "\n"
        else:
            modified_content += line + "\n"
    
    with open(output_file, "w") as f:
        f.write(modified_content)
    print(f"Saved content to {output_file}")

if __name__ == "__main__":
    # Fetch content and save to ntv.m3u8
    fetch_and_save_to_file("ntv", "kralpop", "ressources/tur/ntv.m3u8")

    # Fetch content and save to star.m3u8
    fetch_and_save_to_file("star", "kralpop", "ressources/tur/star.m3u8")
