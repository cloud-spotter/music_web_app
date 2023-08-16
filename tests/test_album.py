from lib.album import *

'''
Album constructs with id, title, release_year, artist_id
'''

def test_album_constructs():
    album = Album(1, "Test Album", 2019, 1)
    assert album.id == 1
    assert album.title == "Test Album"
    assert album.release_year == 2019
    assert album.artist_id == 1

'''
Albums with equal contents are equal
'''

def test_compare():
    album1 = Album(1, 'Father of the Bride', 2019, 1)
    album2 = Album(1, 'Father of the Bride', 2019, 1)
    assert album1 == album2
    
'''
Albums represent as strings
'''
def test_stringify_album_object():
    album = Album(1, 'Father of the Bride', 2019, 1)
    assert str(album) == "Album(1, Father of the Bride, 2019, 1)"