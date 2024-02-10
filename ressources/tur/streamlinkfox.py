import streamlink
session = streamlink.Streamlink()
streams = session.streams('https://www.fox.com.tr/canli-yayin', http_ssl_verify=False)
print(streams["best"].multivariant.uri)
