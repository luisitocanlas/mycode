#!usr/bin/env python3

import requests
import pprint

# API endpoint
endpoint = 'https://pokeapi.co/api/v2/pokemon/'

def main():
    num = input('Pick a number between 1 and 151!\n> ')

    jsonData = requests.get(endpoint + num).json()
    
    # print the keys
    # print(jsonData.keys())

    # get name
    pokemonName = jsonData['name'].title()

    # get the sprite URL
    pokemonImg = jsonData['sprites']['front_default']

    # get all the names of all the moves of the pokemon
    pokemonMoves = []

    for move in jsonData['moves']:
        pokemonMoves.append(move['move']['name'])

    # get the number of games the pokemon appeared in
    gameList = []
    counter = 0
    for game in jsonData['game_indices']:
        counter += 1
        gameList.append(game['version']['name'].title())

    print(f'''
Pokemon: {pokemonName}\n
Img: {pokemonImg}\n
Moves: {pokemonMoves}\n
Games: {gameList}\n
Number of Games: {counter}
    ''')
    

if __name__ == '__main__':
    main()