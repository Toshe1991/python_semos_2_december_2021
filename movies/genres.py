import requests
from requests import RequestException
import datetime

'''
[{'id': 12, 'name': 'Adventure'}, {'id': 14, 'name': 'Fantasy'}, {'id': 16, 'name': 'Animation'}, 
{'id': 18, 'name': 'Drama'}, {'id': 27, 'name': 'Horror'}, {'id': 28, 'name': 'Action'}, 
{'id': 35, 'name': 'Comedy'}, {'id': 36, 'name': 'History'}, {'id': 37, 'name': 'Western'}, 
{'id': 53, 'name': 'Thriller'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, 
{'id': 878, 'name': 'Science Fiction'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10402, 'name': 'Music'}, 
{'id': 10749, 'name': 'Romance'}, {'id': 10751, 'name': 'Family'}, {'id': 10752, 'name': 'War'}, 
{'id': 10770, 'name': 'TV Movie'}]
'''


class Genres:
    URL = "https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}&language=en-US"
    genres = []

    def __init__(self, api_key):
        self.fetch_time = datetime.datetime.now()
        self.api_key = api_key
        self.fetch_genres_list()

    def fetch_genres_list(self):
        try:
            data = requests.get(self.URL.format(api_key=self.api_key)).json()
        except RequestException:
            print("Error happened while fetching data for genres.")
            return

        self.genres = data["genres"]
        self.genres.sort(key=lambda val: val["id"])

    def get_genre_name_by_id(self, genre_id):
        """
        Return the name of the genre based on the ID.
        :parameter genre_id: id of the genre
        :return: Name of the genre
        """
        # Za doma, procitajte sto e Binary Search, i probajte da go smenite ovoj metod
        # da koristi binary search
        for genre in self.genres:
            if genre["id"] == genre_id:
                return genre["name"]

        raise Exception(f"Genre with id {genre_id}, doesn't exist.")

    def genre_id_by_name(self, genre_name):
        """
        Return the id of the genre based on the genre name.
        :param genre_name: name of the genre to find
        :return: id of the found genre
        """
        for genre in self.genres:
            if genre["name"] == genre_name:
                return genre["id"]

        raise Exception(f"Genre with name {genre_name}, doesn't exist.")