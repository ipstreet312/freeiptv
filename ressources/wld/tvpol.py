import streamlink

streams = streamlink.streams('https://vod.tvp.pl/live,1/tvp-polonia,399723')
erstrm = streams["best"].multivariant.uri

print("#EXTM3U")
print("#EXT-X-VERSION:4")
print("#EXT-X-INDEPENDENT-SEGMENTS")
print('#EXT-X-STREAM-INF:BANDWIDTH=4056800,AVERAGE-BANDWIDTH=2741200,CODECS="avc1.640020,mp4a.40.2",RESOLUTION=1024x576,FRAME-RATE=50.000,AUDIO="program_audio_0"')
print(erstrm.replace("master.m3u8", "master_v2.m3u8"))
print(f'#EXT-X-MEDIA:TYPE=AUDIO,LANGUAGE="pol",NAME="Polski",AUTOSELECT=YES,DEFAULT=YES,CHANNELS="2",GROUP-ID="program_audio_0",URI="{erstrm.replace("master.m3u8", "master_a1.m3u8")}"')
