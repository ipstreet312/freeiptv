import requests

# Base URLs for NTV and STAR
ntv_base_url = "https://mn-nl.mncdn.com/dogusdyg_ntv/"
star_base_url = "https://mn-nl.mncdn.com/dogusdyg_star/"
initial_url = "https://dygvideo.dygdigital.com/live/hls/kralpop?m3u8"

def fetch_and_save_m3u8(base_url, modified_url, output_file):
    try:
        # Fetch the content from the modified URL
        content_response = requests.get(modified_url)
        content_response.raise_for_status()
        content = content_response.text

        # Process and save the content
        lines = content.split("\n")
        modified_content = ""

        for line in lines:
            if line.startswith("live_"):
                # Add base URL to live stream lines
                full_url = base_url + line
                modified_content += full_url + "\n"
            else:
                modified_content += line + "\n"
        
        # Save the modified content to the specified output file
        with open(output_file, "w") as f:
            f.write(modified_content)
        print(f"Content saved to {output_file}")

    except requests.RequestException as e:
        print(f"An error occurred while fetching {output_file}: {e}")

try:
    # Fetch the initial URL for NTV
    response = requests.get(initial_url)
    response.raise_for_status()

    # Get the final URL returned by the request
    final_url = response.url

    # Modify the URL to point to NTV variant
    ntv_modified_url = final_url.replace("dogusdyg_kralpoptv/dogusdyg_kralpoptv.smil/playlist", "dogusdyg_ntv/live")
    # Modify the URL to point to STAR variant
    star_modified_url = final_url.replace("dogusdyg_kralpoptv/dogusdyg_kralpoptv.smil/playlist", "dogusdyg_star/live")

    # Fetch and save NTV m3u8 file
    fetch_and_save_m3u8(ntv_base_url, ntv_modified_url, "ressources/tur/ntv.m3u8")

    # Fetch and save STAR m3u8 file
    fetch_and_save_m3u8(star_base_url, star_modified_url, "ressources/tur/star.m3u8")

except requests.RequestException as e:
    print(f"An error occurred while fetching the initial URL: {e}")
