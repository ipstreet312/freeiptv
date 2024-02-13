from streamlink.plugins.foxtr import FoxTR
from streamlink.stream import HLSStream
from streamlink.session import Streamlink

session = Streamlink()
url = 'https://www.nowtv.com.tr/canli-yayin'
plugin = FoxTR(session, url)
streams = plugin._get_streams()
print(streams["best"].multivariant.uri)
