import requests
import re

headers = {
    'Origin': 'https://www.atv.com.tr',
    'Referer': 'https://www.atv.com.tr/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

resp1 = requests.get('https://securevideotoken.tmgrup.com.tr/webtv/secure?000000&url=https%3A%2F%2Ftrkvz.daioncdn.net%2Fatv%2Fatv.m3u8%3Fce%3D3%26app%3Dd1ce2d40-5256-4550-b02e-e73c185a314e', headers=headers).json()

m3u8_url = resp1['Url']
print(f'\n{m3u8_url}\n')

import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}

resp2 = requests.get(m3u8_url, headers=headers).text

atv_list = re.findall(r'#EXT-X-STREAM-INF:.*\n(.*\.m3u8.*)', resp2)

for m3u8_res in atv_list:
    print(f'https://trkvz.daioncdn.net/atv/{m3u8_res}')
