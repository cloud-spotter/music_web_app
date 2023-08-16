# {{ /albums }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# POST /albums

/albums/title=Voyage
/albums/release_year=2022
/albums/artist_id=2

POST /albums (parameters and datatypes)
  title: string
  release_year: int (as str and need to convert) 
  artist_id: int (as str and need to convert)

# GET /albums

```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python

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






# EXAMPLE

# GET /home
#  Expected response (200 OK):
"""
This is my home page!
"""

# GET /wave?name=Leo
#  Expected response (200 OK):
"""
I am waving at Leo
"""

# GET /wave
#  Expected response (200 OK):
"""
I am waving at no one!
"""

# POST /submit
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a message
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /home
  Expected response (200 OK):
  "This is my home page!"
"""
def test_get_home(web_client):
    response = web_client.get('/home')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'This is my home page!'

"""
POST /submit
  Parameters:
    name: Leo
    message: Hello world
  Expected response (200 OK):
  "Thanks Leo, you sent this message: "Hello world""
"""
def test_post_submit(web_client):
    response = web_client.post('/submit', data={'name': 'Leo', 'message': 'Hello world'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Thanks Leo, you sent this message: "Hello world"'
```


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
