from lib.album_repository import *
from lib.album import *
from lib.database_connection import *

'''
When I call #all 
I get all the albums in the albums table
'''
def test_all(db_connection):
    db_connection.seed("seeds/album_store.sql")
    repository = AlbumRepository(db_connection)
    assert repository.all() == [
        Album(1, 'Father of the Bride', 2019, 1),
        Album(2, 'London Calling', 1979, 3)]
        #"Album(3, 'Voyage', 2022, 2)"

'''
When I call #create
I create a new album in the database
And I can see it back in #all
'''
def test_create(db_connection):
    db_connection.seed("seeds/album_store.sql")
    repository = AlbumRepository(db_connection)
    album = Album(None, 'Test Title', 1000, 3)
    repository.create(album)
    result = repository.all()
    assert result == [
        Album(1, 'Father of the Bride', 2019, 1),
        Album(2, 'London Calling', 1979, 3),
        Album(3, 'Test Title', 1000, 3)]
