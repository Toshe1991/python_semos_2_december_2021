import requests

from movie import Movie


class MoviesList:
    search_movie_url = "https://api.themoviedb.org/3/search/movie?api_key={api_key}&page={page}&query={query}"
    year_genre_movie_url = "https://api.themoviedb.org/3/discover/movie?api_key={api_key}&" \
                           "sort_by=popularity.desc&page={page}&year={year}&with_genres={genres}"

    def __init__(self, api_key, genres):
        self.api_key = api_key
        self.genres = genres
        self.__movies = []

    # count=10, offset=150 -> range(150, 160)
    def get_movies(self, count, offset=0):
        for movie in self.__movies[offset:offset+count]:
            print(movie)

    def __fetch_movies_list(self, url):
        try:
            movies = requests.get(url).json()
        except requests.RequestException:
            movies = {}

        return movies

    def set_genres(self, movie, genre_ids):
        for genre_id in genre_ids:
            try:
                genre_name = self.genres.get_genre_name_by_id(genre_id)
                movie.add_genre(genre_name)
            except Exception as e:
                print(e)

    def add_movies_to_collection(self, movies):
        for movie in movies:
            obj = Movie(
                id=movie.get("id"),
                title=movie.get("title"),
                release_date=movie.get("release_date")
            )
            self.__movies.append(obj)
            self.set_genres(obj, movie["genre_ids"])

    def search_movie_by_name(self, movie_name):
        """
        Get all movies that include the `movie_name` in their title.
        :param movie_name: name of a movie, or part of movie name.
        :return: count of total movies
        """
        url = self.search_movie_url.format(api_key=self.api_key, page=1, query=movie_name)
        movies = self.__fetch_movies_list(url=url)
        total_movies_found = movies["total_results"]
        total_pages = movies["total_pages"]
        page = movies["page"] + 1
        results = movies["results"]
        self.add_movies_to_collection(results)

        while page <= total_pages and page <= 10:
            url = self.search_movie_url.format(api_key=self.api_key, page=page, query=movie_name)
            movies = self.__fetch_movies_list(url=url)
            page = movies["page"] + 1

        return total_movies_found
