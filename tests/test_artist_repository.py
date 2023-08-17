from lib.artist_repository import *
from lib.database_connection import *

'''
When I call #all 
I get all the artists in the artists table
'''
def test_all(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)
    assert repository.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz')
    ]

'''
When I call #create
I create a new artist in the database
And I can see it back in #all
'''
def test_create(db_connection):
    db_connection.seed("seeds/artists.sql")
    repository = ArtistRepository(db_connection)
    artist = Artist(None, 'Wild nothing', 'Indie')
    repository.create(artist)
    assert repository.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Wild nothing', 'Indie')
    ]