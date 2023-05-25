from __future__ import division
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Pool
from requests import get
import sys, os

def Download_API(id):
    if not os.path.exists("alternative_titles/" + id + ".json"):
        url = "https://api.themoviedb.org/3/movie/" + id + "/alternative_titles?api_key=ed0646253701d7550481764a488b6ded"
        with get(url, timeout=10) as response:
            content = response.content
            with open("alternative_titles/" + id + ".json", "wb") as file:
                file.write(content)

file_path = 'file_names.txt'

with open(file_path, 'r') as file:
    # for line in file:
    #     movie_id = line.strip()  # Remove leading/trailing whitespace or newline characters
    #     # Perform desired operations with each file name
    #     print(file_name)  # Replace with your own code
    movies_id = [line.strip() for line in file]


num_tasks = len(movies_id)
print(num_tasks)

with ThreadPoolExecutor(max_workers=250) as executor:
    futures = [executor.submit(Download_API, id) for id in movies_id]
    for i, _ in enumerate(as_completed(futures), 1):
        sys.stderr.write('\rdone {0:%}'.format(i/num_tasks))