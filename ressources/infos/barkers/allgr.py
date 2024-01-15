import requests

def fetch_content_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from URL: {e}")
        return None

url = "https://raw.githubusercontent.com/ipstreet312/freeiptv/master/all.m3u"
input_text = fetch_content_from_url(url)

if input_text is not None:
    output_lines = []
    current_group_title = None

    for line in input_text.split('\n'):
        if line.startswith('#EXTINF:0'):
            group_title_start = line.find('group-title="')
            if group_title_start != -1:
                group_title_end = line.rfind('"')
                current_group_title = line[group_title_start + 13: group_title_end]

            output_lines.append(line)  # Keep the #EXTINF line as is

        elif 'group-title=' not in line:
            if current_group_title is not None:
                output_lines.append(line.replace(',', f' group-title="{current_group_title}",'))

        else:
            output_lines.append(line)

    output_text = '\n'.join(output_lines)

    output_file_path = "ressources/allgr.m3u"
    with open(output_file_path, "w") as output_file:
        output_file.write(output_text)

    print(output_file_path)
