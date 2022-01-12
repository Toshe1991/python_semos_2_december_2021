import requests
from requests import RequestException

import datetime


API_KEY = "037280345fcab30b7f0fbf6675ee5cc0"


class Genres:
    URL = f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=en-US"
    genres = []

    def __init__(self):
        self.fetch_time = datetime.datetime.now()
        self.fetch_genres_list()

    def fetch_genres_list(self):
        try:
            data = requests.get(self.URL).json()
        except RequestException:
            print("Error happened while fetching data for genres.")
            return

        self.genres = data["genres"]
        self.genres.sort(key=lambda val: val["id"])
