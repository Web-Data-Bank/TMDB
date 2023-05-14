from __future__ import division
from multiprocessing import Pool
from requests import get
import sys

def MidSongLink(id):
    wunder = get("https://api.themoviedb.org/3/movie/"+id+"?api_key=ed0646253701d7550481764a488b6ded", timeout=10)
    open("json/"+id+'.json', 'wb').write(wunder.content)

song_id = [str(i) for i in range(sys.argv[1], sys.argv[1]*1000)]

p = Pool(50)
num_tasks = len(song_id)
print(num_tasks)
for i, _ in enumerate(p.imap_unordered(MidSongLink, song_id), 1):
    sys.stderr.write('\rdone {0:%}'.format(i/num_tasks))