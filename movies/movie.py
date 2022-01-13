
class Movie:

    def __init__(self, id, title, release_date):
        self.id = id
        self.title = title
        self.release_date = release_date
        self.genres = []

    # Write to file za domasna

    def add_genre(self, genre_name):
        self.genres.append(genre_name)

    def __str__(self):
        return f"{self.title} - {self.release_date} - {self.genres}"
