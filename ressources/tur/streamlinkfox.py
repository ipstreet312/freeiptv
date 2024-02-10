import logging
import streamlink
logging.basicConfig(level=logging.DEBUG)
session = streamlink.Streamlink()
session.set_option("http-verify", False)
streams = session.streams('https://www.fox.com.tr/canli-yayin')
print(streams["best"].multivariant.uri)
