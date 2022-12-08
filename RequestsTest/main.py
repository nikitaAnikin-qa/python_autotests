import requests
import json

token = 'c2f4efd395ca9e79f110b62b814b5f1a'
response = requests.post ('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "name": "Qapokemon",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.text)

response_put = requests.put ('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": 1474,
    "name": "QaNikita",
    "photo": ""
})

print(response_put.text)

response = requests.post ('https://pokemonbattle.me:5000//trainers/addPokebol', headers={'trainer_token' : token}, json={
    "pokemon_id": "1477"
})

print(response.text)