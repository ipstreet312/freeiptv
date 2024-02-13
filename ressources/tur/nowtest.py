import streamlink
streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
erstrm = streams["best"].multivariant.uri
dastrm = erstrm.replace("nowtv-live-ad.ercdn.net/nowtv/playlist.m3u8", "nowtv.daioncdn.net/nowtv/nowtv.m3u8")
