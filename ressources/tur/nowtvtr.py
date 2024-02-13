import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
stande = streams["best"].multivariant.uri
query_string = stande.split('?')[1]
print(query_string)
