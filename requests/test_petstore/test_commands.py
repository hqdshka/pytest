import requests
import pytest

url = 'https://petstore.swagger.io/v2/'
def test_get_store():
    response = requests.get(url+'store/inventory')
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('code', 200 ), ('type','unknown'), ('message', 'ok')])
def test_create_user_wArray(key, value):
    response = requests.post(url+'user/createWithArray', json=[{
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
    }])
    assert response.json()[key] == value

@pytest.mark.parametrize('key, value', [('code', 200 ), ('type','unknown')])
def test_login(key, value):
    response = requests.get(url+'user/login', params = {'username':'username','password':'password'})
    assert response.json()[key] == value



def test_put_pet():
    response = requests.put(url+'user/qwerty', json=[
    {
        "id": 0,
        "category": {
        "id": 0,
        "name": "string"
    },
        "name": "doggie",
        "photoUrls": [
        "string"
    ],
        "tags": [
    {
        "id": 0,
        "name": "string"
    }],
        "status": "available"
    }])
    assert response.status_code == 200

