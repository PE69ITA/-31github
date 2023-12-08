import random

def pokemon_randomizer():
    pokemon_list = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu", "Jigglypuff", "Meowth", "Psyduck", "Growlithe", "Eevee", "Snorlax"]

    random_pokemon = random.choice(pokemon_list)

    print(f"Your randomly chosen Pokémon is: {random_pokemon}")

if __name__ == "__main__":
    pokemon_randomizer()
