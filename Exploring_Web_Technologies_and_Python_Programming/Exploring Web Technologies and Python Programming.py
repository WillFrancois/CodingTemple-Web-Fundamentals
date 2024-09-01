import requests
import json

#Task 2
response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu").text
data = json.loads(response)

name = data["name"]
abilities = data["abilities"]

print("Name: " + data["name"])

for i in range(0, len(abilities)):
    print("Ability " + str(i + 1) + ": " + str(abilities[i]["ability"]["name"]))
print()

#Task 3
def fetch_pokemon_data(pokemon_name):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(pokemon_name))
    return json.loads(response.text)

def calculate_average_weight(pokemon_list):
    accumulator = 0

    for pokemon in pokemon_list:
        pkmn_data = fetch_pokemon_data(pokemon)
        print("Pokemon name: " + pokemon)
        print("Abilities:")
        for ability in pkmn_data["abilities"]:
            print(ability["ability"]["name"])
        accumulator += pkmn_data["weight"]
        print()

    print("Average weight: " + str(accumulator / len(pokemon_list)))
    return accumulator / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

calculate_average_weight(pokemon_names)
