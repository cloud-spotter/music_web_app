# Tests for your routes go here













# === Example Code Below ===

#Examples from hello_web_project test_app.py file:

# === 03 Test-driving a route: Exercise Two ===

'''
SORT ROUTE
POST /sort-names
    Parameters:
    names: Joe,Alice,Zoe,Julia,Kieran
Expected response (200 OK)
'''
def test_sort_names_gets_200_OK_status(web_client):
    response = web_client.post('/sort-names', data={'text': "Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

'''
POST /submit
    Parameters: none
    Expected response (400 Bad Request)
'''
def test_sort_names_returns_400_with_no_parameters(web_client):
    response = web_client.post('/sort-names', data={'text': ''})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please provide a list of strings (comma-separated)"
# HAD TO ASK PEERS FOR HELP ON THIS ONE!

# === 03 Test-driving a route: Challenge ===

'''
# GET /names
#   Expected response (200 OK)
'''
"""
Julia, Alice, Karim, Eddie
"""
def test_add_name(web_client):
    #Simulate sending a GET request to /wave
    response = web_client.get('/name')
    #Assert that the status code was 200 (OK)
    assert response.status_code == 200 #passed! At last!
    assert response.data.decode('utf-8') == "Julia,Alice,Karim"

# GET /names?add=Eddie
# Expected response is the string returned with Eddie added
# Expected status_code == 200 (OK)

def test_add_name_to_names(web_client):
    response = web_client.get('/name?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Julia,Alice,Karim,Eddie"


# === End Example Code ===
