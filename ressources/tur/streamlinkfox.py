import streamlink

streams = streamlink.streams('https://www.fox.com.tr/canli-yayin')
best_quality_stream = streams.get('best')

if best_quality_stream:
    best_quality_urls = best_quality_stream.url

    if isinstance(best_quality_urls, list):
        for url in best_quality_urls:
            if url.startswith('https://foxtv.daioncdn.net/foxtv/foxtv.m3u8'):
                print(url)
                break
        else:
            print("No matching URL found in 'best' quality.")
    else:
        if best_quality_urls.startswith('https://foxtv.daioncdn.net/foxtv/foxtv.m3u8'):
            print(best_quality_urls)
        else:
            print("The 'best' quality URL does not match the expected pattern.")
else:
    print("Either 'best' quality does not exist or it is not an HLSStream instance.")


