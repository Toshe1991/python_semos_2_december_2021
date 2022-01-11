# import requests

# response = requests.get("https://api.themoviedb.org/3/movie/550?api_key=037280345fcab30b7f0fbf6675ee5cc0")
# print(response.json())

from genres import Genres

genres = Genres()
print(genres.genres)
