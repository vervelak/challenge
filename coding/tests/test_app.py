import json

def test_multiple_of_seven(app, client):
    del app
    response = client.get('/api/v1/14')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == 'E'
    
def test_multiple_of_nine(app, client):
    del app
    response = client.get('/api/v1/18')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == 'G'

def test_multiple_of_seven_and_nine(app, client):
    del app
    response = client.get('/api/v1/63')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == 'EG'