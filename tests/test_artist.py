from lib.artist import *

'''
Artist constructs with id, name and genre
'''
def test_artist_constructs():
    artist = Artist(1, "Test Artist", "Pop")
    assert artist.id == 1
    assert artist.name == "Test Artist"
    assert artist.genre == "Pop"

'''
Artists with equal contents are equal
'''
def test_compare():
    artist1 = Artist(1, 'Pixies', 'Rock')
    artist2 = Artist(1, 'Pixies', 'Rock')
    assert artist1 == artist2

