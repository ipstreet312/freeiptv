import streamlink
streams = streamlink.streams('https://www.media.gov.kw/LiveTV.aspx?PanChannel=KTV1')
print(streams["best"])
