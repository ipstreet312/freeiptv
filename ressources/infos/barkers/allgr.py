import requests

def fetch_content_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL: {e}")
        return None

def parse_entries(input_text):
    lines = input_text.strip().split('\n')
    output_lines = []
    current_group_title = None

    for line in lines:
        if line.startswith("#EXTINF"):
            group_title_start = line.find('group-title="')
            if group_title_start != -1:
                group_title_end = line.find('"', group_title_start + 13)
                current_group_title = line[group_title_start + 13 : group_title_end]
            output_lines.append(line)
        elif line.startswith("#EXT"):
            if current_group_title is not None:
                output_lines[-1] += f' group-title="{current_group_title}",'
            output_lines.append(line)
            current_group_title = None
        else:
            output_lines.append(line)

    return '\n'.join(output_lines)

# Example usage:
url = "https://raw.githubusercontent.com/ipstreet312/freeiptv/master/all.m3u"
input_text = fetch_content_from_url(url)

if input_text is not None:
    output_text = parse_entries(input_text)

    # Write to a file
    output_file_path = "allgr.m3u"
    with open(output_file_path, "w") as output_file:
        output_file.write(output_text)

    print(f"Output written to {output_file_path}")
