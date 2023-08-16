class Album:
    def __init__(self, id, title, release_year, artist_id) -> None:
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # Assert that the objects it expects are the objects we made 
    # based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # Prints album object as a string for readability
    def __repr__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id})"