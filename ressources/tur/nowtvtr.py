import streamlink

def main():
    streams = streamlink.streams('https://www.nowtv.com.tr/canli-yayin')
    erstrm = streams["best"].multivariant.uri
    donstrm = erstrm.replace('nowtv-live-ad.ercdn.net/nowtv/playlist', 'nowtv.daioncdn.net/nowtv/nowtv')
    print(erstrm)
    print(donstrm)

if __name__ == "__main__":
    main()
