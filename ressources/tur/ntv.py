import sys
import requests

def fetch_and_print_from_url(base_url, variant):
    initial_url = f"https://dygvideo.dygdigital.com/live/hls/{variant}?m3u8"

    try:
        response = requests.get(initial_url)
        response.raise_for_status()

        final_url = response.url
        modified_url = final_url.replace(f"dogusdyg_{variant}/dogusdyg_{variant}.smil/playlist", f"dogusdyg_{base_url}/live")

        content_response = requests.get(modified_url)
        content_response.raise_for_status()
        content = content_response.text
        
        process_content(content, base_url)

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

def fetch_and_print_from_file(file_path, base_url):
    try:
        with open(file_path, "r") as file:
            content = file.read()
        
        process_content(content, base_url)

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_content(content, base_url):
    lines = content.split("\n")
    modified_content = ""

    for line in lines:
        if line.startswith("live_"):
            full_url = f"https://mn-nl.mncdn.com/dogusdyg_{base_url}/" + line
            modified_content += full_url + "\n"
        else:
            modified_content += line + "\n"
    
    print(modified_content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # If arguments are provided, use file-based processing
        if len(sys.argv) < 3:
            print("Usage: python3 yourpython.py <ntv_file_path> <star_file_path>")
            sys.exit(1)

        ntv_file_path = sys.argv[1]
        star_file_path = sys.argv[2]

        # Process NTV file
        fetch_and_print_from_file(ntv_file_path, "ntv")

        # Process STAR file
        fetch_and_print_from_file(star_file_path, "star")
    else:
        # If no arguments are provided, use URL-based fetching
        print("No files provided, fetching content from URLs...")

        # Fetch for NTV variant
        fetch_and_print_from_url("ntv", "kralpop")

        # Fetch for STAR variant
        fetch_and_print_from_url("star", "kralpop")
