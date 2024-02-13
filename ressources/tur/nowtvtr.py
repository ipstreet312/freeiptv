import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
erstrm = streams["best"].multivariant.uri
print(erstrm)
donstrm = erstrm.replace('nowtv-live-ad.ercdn.net/nowtv/playlist', 'nowtv.daioncdn.net/nowtv/nowtv')
print(donstrm)
