import streamlink
your_dictionary = {
    'best': ['your_best_url_1', 'your_best_url_2'],
}
streams = streamlink.streams('https://www.fox.com.tr/canli-yayin', your_dictionary['best'])
master_url = streams['best'][1]
print(master_url)
