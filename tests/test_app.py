# Tests for your routes go here
import os
from lib.database_connection import get_flask_database_connection
from flask import Flask, request


#####-----  Scenario 1  -----#####

#POST (create albums table row entry):
# POST /album
#  Parameters:
#    title: 'Voyage'
#    release_year: 2022
#    artist_id: 2

# Expected response (200 OK):
"""
"""   
# (No content returned)

#GET (request list of albums from table):

# GET /album
# Expected response (200 OK)
"""
Album(3, Voyage, 2022, 2)
"""

'''
When: I call POST /albums with album info
That album is now in the list in GET /albums
'''
def test_post_album_table_populates_with_album(db_connection, web_client):
    db_connection.seed("seeds/album_store.sql")
    post_response = web_client.post("/albums", data={
        'title': 'Voyage',
        'release_year': '2022', #Remember: everything sent via a Request is a string
        'artist_id': '2'
    })
    assert post_response.status_code == 200 
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/albums")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Album(1, Father of the Bride, 2019, 1)\n" \
        "Album(2, London Calling, 1979, 3)\n" \
        "Album(3, Voyage, 2022, 2)"
    
'''
When I call GET /albums
I get a list of albums back
'''
def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/album_store.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Father of the Bride, 2019, 1)\n" \
        "Album(2, London Calling, 1979, 3)"
    # As a single line string:
    # assert response.data.decode('utf-8') == "Album(1, Father of the Bride, 2019, 1)\nAlbum(2, London Calling, 1979, 3)"

#####-----  Scenario 2  -----#####

    #POST (request sent without parameters):
    # POST /album

    # Expected response (400 Bad Request):
    """
    You need to submit a title, release_year and artist_id
    """  

    # GET /album
    # Expected response (200 OK)
    """
    Album(Father of the Bride, 2019, 1)
    Album(London Calling, 1979, 3)
    """

# ^ Not implemented




#####-----  Scenario 1  /artists -----#####

# GET /artists
# Expected response (200 OK):
"""
Pixies, ABBA, Taylor Swift, Nina Simone
""" 
'''
When I call GET /artists
I get a list of artists back 
'''
def test_get_artists(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone'

#####-----  Scenario 2  -----#####

# POST /artist
#  Parameters:
#    name: "Wild_nothing"
#    genre: "Indie"

# Expected response (200 OK):
"""
"""   
# (No content returned)


#GET (to confirm artist added):

# GET /artist
# Expected response (200 OK)
"""
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing
"""

#Tests:
'''
When: I call POST /artists with artist info
That artist is now in the list in GET /artists
'''
def test_post_artists(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    post_response = web_client.post("/artists", data={
        'name': 'Wild_nothing',
        'genre': 'Indie'
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""

    get_response = web_client.get("/artists")
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild_nothing'

'''
When I call GET /artists
I get a list of artists back
With the added artist in the list
'''
def test_get_artists_after_update(db_connection, web_client):
    db_connection.seed("seeds/artists.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Pixies, ABBA, Taylor Swift, Nina Simone, Wild_nothing'