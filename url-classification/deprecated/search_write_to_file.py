import json
from search_query import search
import time
def search_and_write(dates_from, dates_to):
    for i in range(len(dates_from)):
        data = search(dates_from[i], dates_to[i], 5)
        with open(f'data/data{i}.txt', 'w') as outfile:
            json.dump(data, outfile)
        time.sleep(2)