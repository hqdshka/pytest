import requests

url = 'https://petstore.swagger.io/v2/'
response = requests.get(url+'store/inventory')
if response.status_code == 200:
    print(response.text)
else:
    print('Ошибка, пришел код', response.status_code, 'а не 200')

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
if response.status_code == 200:
    print(response.text)
else:
    print('Ошибка, пришел код', response.status_code, 'а не 200')

response = requests.get(url+'user/login', params = {'username':'username','password':'password'})
if response.status_code == 200:
    code_ok = response.json()['code']
    print(response.text)
    print(code_ok)
else:
    print('Ошибка, пришел код', response.status_code, 'а не 200')

response = requests.put(url+'pet', json=[
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
if response.status_code == 200:
    code_ok = response.json()[code]
    print(response.text)
    
else:
    print('Ошибка, пришел код', response.status_code, 'а не 200')