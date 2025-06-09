import streamlink

streams = streamlink.streams('vod.tvp.pl/live,1/tvp-world,399731')
erstrm = streams["best"].multivariant.uri

print("#EXTM3U")
print("#EXT-X-VERSION:5")
print('#EXT-X-STREAM-INF:BANDWIDTH=4858000,AVERAGE-BANDWIDTH=4416000,CODECS="mp4a.40.2,avc1.640020",RESOLUTION=1280x720,FRAME-RATE=50,VIDEO-RANGE=SDR,AUDIO="audio-aacl-211",CLOSED-CAPTIONS=NONE"')
print(erstrm.replace("master.m3u8", "TVP_World-audio_211682_pol=211200-video=3954400.m3u8"))
