from __future__ import division
from multiprocessing import Pool
from requests import get
import sys, os


def MidSongLink(id):
    if not os.path.exists("json/" + id + ".json"):
        url = "https://api.themoviedb.org/3/movie/" + id + "?api_key=ed0646253701d7550481764a488b6ded"
        with get(url, timeout=10) as response:
            content = response.content
            with open("json/" + id + ".json", "wb") as file:
                file.write(content)
    return 1
    
def main():
    # a = int(sys.argv[1])
    song_id = [str(i) for i in range(1, 1131088)]

    pool_size = 250  # Adjust the pool size as per system capabilities
    num_tasks = len(song_id)
    print(num_tasks)

    with Pool(pool_size) as p:
        for i, _ in enumerate(p.imap_unordered(MidSongLink, song_id), 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_tasks))

if __name__ == "__main__":
    main()