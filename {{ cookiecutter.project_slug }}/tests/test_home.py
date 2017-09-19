def test_page_title(client):
    response = client.get('/')
    assert '<title>{{ cookiecutter.project_name }}</title>' in response.content.decode('utf-8')
