from yt_dlp import YoutubeDL

url = 'https://hls-players.dzsecurity.net/live/player/elhayattv'

ydl_opts = {
    'quiet': True,
    'skip_download': True,
    'force_generic_extractor': True,
    'http_headers': {
        'Referer': 'https://elhayat.dz/'
    }
}

with YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(url, download=False)
    formats = info_dict.get('formats', [])
    for f in formats:
        if f.get('ext') == 'm3u8':
            m3u8_url = f.get('url')
            print(f'Found m3u8 URL: {m3u8_url}')
            break
    else:
        print('No m3u8 URL found.')
