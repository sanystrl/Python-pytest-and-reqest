import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5f56a154343066786869100aa3e7dfaf'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "generate",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_change = {
    "pokemon_id": pokemon_id,
    "name": "New Name 333",
    "photo_id": 26
}

body_catch = {
    "pokemon_id" : pokemon_id
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)