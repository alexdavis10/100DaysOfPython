import requests

pokemon_name = input("Enter the name of the pokemon: ")
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
response = requests.get(url)

if response.status_code == 200:
    pokemon_data = response.json()
    print(f"Name: {pokemon_data['name'].capitalize()}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")

    types = [t['type']['name'] for t in pokemon_data['types']]
    print(f"Types: {', '.join(types)}")

    weaknesses = []
    for t in pokemon_data['types']:
        type_url = t['type']['url']
        type_response = requests.get(type_url)
        type_data = type_response.json()
        damage_relations = type_data['damage_relations']
        for weakness in damage_relations['double_damage_from']:
            weaknesses.append(weakness['name'])

    print(f"Weaknesses: {', '.join(weaknesses)}")
else:
    print("Pokemon not found.")
