import datetime

from .genres import Genres

my_genres = Genres(api_key=)


def test_object_built():
    assert isinstance(my_genres.fetch_time, datetime.datetime)
    assert len(my_genres.genres) != 0


def test_get_genre_name_by_id():
    assert my_genres.get_genre_name_by_id(80) == "Crime"


def test_get_genre_name_by_id_invalid():
    try:
        my_genres.get_genre_name_by_id(-1)
    except Exception as e:
        assert str(e) == "Genre with id -1, doesn't exist."
