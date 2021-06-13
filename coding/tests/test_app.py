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

def test_not_multiple_positive(app, client):
    del app
    response = client.get('/api/v1/33')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == 33

def test_not_multiple_negative(app, client):
    del app
    response = client.get('/api/v1/-33')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == -33

def test_float(app, client):
    del app
    response = client.get('/api/v1/0.312')
    assert response.status_code == 404

def test_str(app, client):
    del app
    response = client.get('/api/v1/abc')
    assert response.status_code == 404