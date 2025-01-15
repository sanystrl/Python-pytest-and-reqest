import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5f56a154343066786869100aa3e7dfaf'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '12289'

def test_status_code():
    respons = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert respons.status_code == 200

def test_part_of_response():
    resposponse_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert resposponse_get.json()["data"][0]["name"] == 'New Name 333'


@pytest.mark.parametrize('key, value', [('name', 'New Name 333'),('trainer_id', TRAINER_ID),('id', '194554')])
def test_parametrize(key, value):
    resposponse_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert resposponse_parametrize.json()["data"][0][key] == value