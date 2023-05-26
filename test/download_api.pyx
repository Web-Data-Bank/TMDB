# cython: language_level=3
import os
from requests import get

def Download_API(str id):
    if not os.path.exists("alternative_titles/" + id + ".json"):
        url = "https://api.themoviedb.org/3/movie/" + id + "/alternative_titles?api_key=ed0646253701d7550481764a488b6ded"
        with get(url, timeout=10) as response:
            content = response.content
            with open("../alternative_titles/" + id + ".json", "wb") as file:
                file.write(content)
