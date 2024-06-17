import sys
import requests

github_url = "https://raw.githubusercontent.com/Paradise-91/ParaTV/main/streams/nrj/nrj12.m3u8"
base_nrj12 = "https://event1.nrjaudio.fm/hls/live/2038378/nrj_12/"
base_cherie25 = "https://event2.nrjaudio.fm/hls/live/2038379/cherie_25/"

headers = {
    'User-Agent': 'SmartOs Tv'
}

def fetch_nrj12_content(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        lines = response.text.splitlines()

        # Fetch the content of the third link
        if len(lines) > 2:
            third_link = lines[2]
            third_response = requests.get(third_link, headers=headers)
            third_response.raise_for_status()
            third_content = third_response.text.splitlines()

            # Construct full URLs
            updated_lines = []
            for line in third_content:
                if line.startswith("hdntl="):
                    updated_lines.append(base_nrj12 + line)
                else:
                    updated_lines.append(line)

            return "\n".join(updated_lines)
        else:
            raise ValueError("The file does not contain enough links.")
    except Exception as e:
        raise RuntimeError(f"Failed to fetch content: {e}")

def generate_cherie25_content(string):
    return string.replace(base_nrj12, base_cherie25)

def write_to_file(content, output_file):
    try:
        with open(output_file, 'w') as file:
            file.write(content)
        print(f"Generated file: {output_file}")
    except Exception as e:
        raise RuntimeError(f"Failed to write to file {output_file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 nrj12.py <output_file_nrj12> <output_file_cherie25>")
        sys.exit(1)
    
    try:
        nrj12_content = fetch_nrj12_content(github_url)
        cherie25_content = generate_cherie25_content(nrj12_content)
        
        write_to_file(nrj12_content, sys.argv[1])
        write_to_file(cherie25_content, sys.argv[2])
        
    except Exception as e:
        print(f"An error occurred: {e}")
