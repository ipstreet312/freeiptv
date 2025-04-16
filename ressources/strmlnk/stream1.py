from streamlink import Streamlink

session = Streamlink()
streams = session.streams('https://www.nowtv.com.tr/canli-yayin')

# Try to prioritize 'dash', then 'best', or just get any stream
for quality in ["dash", "best"]:
    if quality in streams:
        stream = streams[quality]
        break
else:
    print("No suitable stream found.")
    exit(1)

# Check if the stream is multivariant (e.g., HLS master playlist)
if hasattr(stream, "multivariant") and stream.multivariant:
    erstrm = stream.multivariant.uri
else:
    # Fallback to regular stream URL
    erstrm = stream.to_url()

print(erstrm)

print("Available stream qualities:", list(streams.keys()))
