import os
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import *
from lib.artist_repository import *
from lib.artist import *
from flask import Flask, request, Response

# Create a new Flask app
app = Flask(__name__)

# == /albums routes ==
@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None, 
        request.form['title'], 
        request.form['release_year'],
        request.form['artist_id'])
    repository.create(album)
    return "", 200

@app.route('/albums', methods=['GET']) #Can actually leave the methods parameter out
                                        #here as GET is the default method
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(f"{album}" for album in repository.all())


# == /artists routes ==
@app.route('/artists', methods=['GET']) #@app is a decorator inside the Flask library
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artist_names = []
    for artist in artists:
        artist_names.append(artist.name)
    return ", ".join(artist_names)
    #return 200, "\n".join(f"{artist}" for artist in repository.all())

# Try displaying each side of the assertion statement in the error messages
# to compare (printing won't help always when you're dealing with strings/lists)

# '["Pixies","ABBA","Taylor Swift","Nina Simone"]\n'    
# ['Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone']

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None, 
        request.form['name'], 
        request.form['genre']
    )
    repository.create(artist)
    return "", 200

@app.route('/artists', methods=['GET']) #@app is a decorator inside the Flask library
def get_artists_after_update():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    artist_names = []
    for artist in artists:
        artist_names.append(artist.name)
    return ", ".join(artist_names)



# == Example Code Below ==

# Examples from hello_web_project app.py!

#Request (03 Test-driving a route: Exercise One)
@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    vowels = 'aeiou'
    count = 0
    text = request.form['text'] 
    for char in text:
        if char in vowels:
            count += 1
    return f'There are {count} vowels in "{text}"'

#Request (03 Test-driving a route: Exercise Two)
@app.route('/sort-names', methods=["POST"])
def sort_names():
    # Code block for 200 OK status and returning sorted names:
    # text = request.form['text']
    # split_text = text.split(",")
    # split_text.sort()
    # split_text_as_string = (',').join(split_text)
    # return split_text_as_string
    
    # With 400 RESPONSE FOR NONE PARAMETER:
    text = request.form['text']
    if text == '':
        return Response("Please provide a list of strings (comma-separated)", status=400)
    else:
        split_text = text.split(",")
        split_text.sort()
        split_text_as_string = (',').join(split_text)
        return split_text_as_string

#Request (03 Test-driving a route: Challenge)
@app.route('/name', methods=["GET"])
def add_name():
    predefined_names = ["Julia,Alice,Karim"]
    added_name = request.args.get('add')
    if added_name:
        predefined_names.append(added_name)
    return ",".join(predefined_names)



# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

