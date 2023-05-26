from __future__ import division
from concurrent.futures import ThreadPoolExecutor, as_completed
import sys
from download_api import Download_API

file_path = '../file_names.txt'

with open(file_path, 'r') as file:
    movies_id = [line.strip() for line in file]

num_tasks = len(movies_id)
print(num_tasks)

with ThreadPoolExecutor(max_workers=250) as executor:
    futures = [executor.submit(Download_API, id) for id in movies_id]
    for i, _ in enumerate(as_completed(futures), 1):
        sys.stderr.write('\rdone {0:%}'.format(i/num_tasks))
