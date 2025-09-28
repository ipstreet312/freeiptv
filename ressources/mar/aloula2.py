#!/usr/bin/env python3
import requests
from urllib.parse import parse_qs, urljoin
import argparse

def fetch_token(api_url):
    """Fetch token from EasyBroadcast API."""
    try:
        resp = requests.get(api_url, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Could not retrieve token: {e}")

    data = parse_qs(resp.text)
    if not all(k in data for k in ("token", "token_path", "expires")):
        raise RuntimeError("Invalid token response format.")

    return data["token"][0], data["token_path"][0], data["expires"][0]

def fetch_playlist(signed_url):
    """Fetch playlist content from signed URL."""
    try:
        resp = requests.get(signed_url, timeout=5)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Could not fetch playlist: {e}")

    return resp.text

def rewrite_playlist(playlist_text, base_url, token, token_path, expires):
    """Rewrite segment URLs in playlist to include token parameters."""
    rewritten_lines = []
    for line in playlist_text.splitlines():
        if line.startswith("#") or not line.strip():
            rewritten_lines.append(line)
        else:
            abs_url = urljoin(base_url, line.strip())
            signed_seg = f"{abs_url}?token={token}&token_path={token_path}&expires={expires}"
            rewritten_lines.append(signed_seg)
    return "\n".join(rewritten_lines)

def main():
    parser = argparse.ArgumentParser(description="Fetch and rewrite EasyBroadcast M3U8 playlist.")
    parser.add_argument("--output", "-o", help="Output file (if omitted, prints to stdout)")
    args = parser.parse_args()

    base_url = "https://cdn.live.easybroadcast.io/abr_corp/73_aloula_w1dqfwm/corp/73_aloula_w1dqfwm_480p/chunks_dvr.m3u8"
    token_api_url = f"https://token.easybroadcast.io/all?url={base_url}"

    # Fetch token
    token, token_path, expires = fetch_token(token_api_url)

    # Build signed playlist URL
    signed_url = f"{base_url}?token={token}&token_path={token_path}&expires={expires}"

    # Fetch playlist
    playlist_text = fetch_playlist(signed_url)

    # Rewrite segment URLs
    rewritten_playlist = rewrite_playlist(playlist_text, base_url, token, token_path, expires)

    # Output
    if args.output:
        with open(args.output, "w") as f:
            f.write(rewritten_playlist)
        print(f"Rewritten playlist saved to {args.output}")
    else:
        print(rewritten_playlist)

if __name__ == "__main__":
    main()
