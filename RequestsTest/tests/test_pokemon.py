import requests
import pytest

def test_status_cod():
    response = requests.get ('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200

def test_peace_body():
    response = requests.get ('https://pokemonbattle.me:5000/trainers', params={'trainer_id': '1239'})
    assert response.json()['trainer_name'] == 'SaM'
    


