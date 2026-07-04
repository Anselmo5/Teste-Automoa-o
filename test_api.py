import requests


def test_create_post():

    url = "https://jsonplaceholder.typicode.com/posts"

    data = {
        "title": "Meu Post",
        "body": "Conteúdo do Post",
        "userId": 1
    }

    response = requests.post(url, json=data)

    assert response.status_code == 201

    body = response.json()

    assert body["title"] == data["title"]
    assert body["body"] == data["body"]
    assert body["userId"] == data["userId"]
    assert "id" in body


def test_get_invalid_post():

    url = "https://jsonplaceholder.typicode.com/posts/999999"

    response = requests.get(url)

    assert response.status_code == 404


def test_validate_data_types():

    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    assert response.status_code == 200

    body = response.json()

    assert isinstance(body["id"], int)
    assert isinstance(body["userId"], int)
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)


def test_response_time():

    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url)

    response_time = response.elapsed.total_seconds() * 1000

    assert response_time < 500