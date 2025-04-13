import streamlink

streams = streamlink.streams('https://stream.tvp.pl/?channel_id=1455')
erstrm = streams["best"].multivariant.uri
print(erstrm)

print("#EXTM3U")
print("#EXT-X-VERSION:4")
print("#EXT-X-INDEPENDENT-SEGMENTS")
print('#EXT-X-STREAM-INF:BANDWIDTH=4056800,AVERAGE-BANDWIDTH=2741200,CODECS="avc1.640020,mp4a.40.2",RESOLUTION=1024x576,FRAME-RATE=50.000,AUDIO="program_audio_0"')
print(erstrm.replace("master.m3u8", "master_v2.m3u8"))
print(f'#EXT-X-MEDIA:TYPE=AUDIO,URI="{erstrm.replace("master.m3u8", "master_a1.m3u8")}"')
