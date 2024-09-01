import requests
import json

#Task 2
def fetch_planet_data(should_print=True):
    response = requests.get("https://api.le-systeme-solaire.net/rest/bodies")
    data = json.loads(response.text)
    bodies = data["bodies"]

    for body in bodies:
        if body["isPlanet"] and should_print:
            name = body["englishName"]
            mass = body["mass"]["massValue"]
            orbit_period = body["sideralOrbit"]
            print("Name: " + str(name))
            print("Mass: " + str(mass))
            print("Orbit Period: " + str(orbit_period) + " days")
            print()

    return bodies

#Task 3
def find_heaviest_planet(planets):
    bodies = fetch_planet_data(False)
    mass_list = []

    for body in bodies:
        if body["isPlanet"]:
            mass_list.append((body["englishName"], body["mass"]["massValue"]))

    return max(mass_list, key=lambda x: x[1])

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")
