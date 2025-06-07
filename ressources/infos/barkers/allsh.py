import requests
import os

def fetch_content_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL: {e}")
        return None

def simplify_m3u_text(input_text):
    lines = input_text.splitlines()
    simplified_lines = ['#EXTM3U']
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if line.startswith('#EXTINF'):
            # Extract channel name after the last comma
            if ',' in line:
                name = line.split(',')[-1]
                simplified_lines.append(f'#EXTINF:-1,{name}')
        elif line.startswith('http'):
            simplified_lines.append(line)
    
    return '\n'.join(simplified_lines)

# Main logic
url = "https://raw.githubusercontent.com/ipstreet312/freeiptv/master/all.m3u"
input_text = fetch_content_from_url(url)

if input_text:
    output_text = simplify_m3u_text(input_text)
    
    # Ensure directory exists
    output_file_path = "ressources/allsh.m3u"
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    with open(output_file_path, "w", encoding="utf-8") as output_file:
        output_file.write(output_text)
        print(f"Simplified M3U saved to: {output_file_path}")
