from streamlink.plugins.foxtr import FoxTR
from streamlink.stream import HLSStream
from streamlink.session import Streamlink

session = Streamlink()
url = 'https://www.nowtv.com.tr/canli-yayin'
plugin = FoxTR(session, url)
streams = plugin._get_streams()

if streams:
    best_stream = streams.get('best')
    if best_stream:
        print(best_stream.url)
    else:
        print("No best quality stream found.")
else:
    print("No streams found.")
