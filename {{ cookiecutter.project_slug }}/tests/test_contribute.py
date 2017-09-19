def test_contribute_json(client):
    response = client.get('/contribute.json')
    assert response.status_code == 200
    assert response['Content-Type'] == 'application/json'
