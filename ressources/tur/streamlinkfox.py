import streamlink
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin')
best_quality_stream = streams.get('best')
if best_quality_stream:
    best_quality_urls = best_quality_stream.url
    if isinstance(best_quality_urls, list) and len(best_quality_urls) >= 2:
        second_url_of_best = best_quality_urls[1]
        print(second_url_of_best)
    else:
        print("The 'best' quality does not have at least two URLs.")
else:
    print("Either 'best' quality does not exist or it is not an HLSStream instance.")
