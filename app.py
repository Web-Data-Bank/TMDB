import concurrent.futures
import requests
import sys

def MidSongLink(id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ed0646253701d7550481764a488b6ded".format(id)
    with requests.Session() as session:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        with open("json/{}.json".format(id), 'wb') as file:
            file.write(response.content)

def main():
    a = int(sys.argv[1])
    song_id = [str(i) for i in range(a, a + 250)]

    num_tasks = len(song_id)
    print(num_tasks)

    with concurrent.futures.ThreadPoolExecutor(max_workers=75) as executor:
        futures = [executor.submit(MidSongLink, id) for id in song_id]
        for i, _ in enumerate(concurrent.futures.as_completed(futures), 1):
            sys.stderr.write('\rdone {0:%}'.format(i/num_tasks))

if __name__ == '__main__':
    main()
