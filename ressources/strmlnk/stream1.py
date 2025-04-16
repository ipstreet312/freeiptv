from streamlink import Streamlink

session = Streamlink()
streams = session.streams('https://stream.tvp.pl/?channel_id=1455')

# Try to prioritize 'dash', then 'best', or just get any stream
for quality in ["dash", "best"]:
    if quality in streams:
        stream = streams[quality]
        break
else:
    print("No suitable stream found.")
    exit(1)
    
"""print(stream)
"""

# Check if the stream is multivariant (e.g., HLS master playlist)
if hasattr(stream, "multivariant") and stream.multivariant:
    erstrm = stream.multivariant.uri
else:
    # Fallback to regular stream URL
    erstrm = stream.to_url()

print(erstrm)

print("Available stream qualities:", list(streams.keys()))
