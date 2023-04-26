#!usr/bin/env python3

patrick_star = {
    'species': 'Starfish',
    'occupation': 'Unemployed',
    'residence': 'Bikini Bottom',
    'best_friend': 'SpongeBob SquarePants',
    'hobbies': ['sleeping', 'eating', 'rock collecting'],
    }

# add new key/value pair
patrick_star["relatives"] = ["Herb Star", "Margie Star", "Sam Star", "Squidina Star"] 

# print a list of all the keys
# print(patrick_star.keys())

# ask user for input and save it
# choice = input("Select from the list above:\n> ")

# # bonus
# if choice not in patrick_star:
#     print(f'{choice} is not in the list!')
# else:
#     # return the value from user input key
#     print(patrick_star[choice])

# super bonus
for i, k in enumerate(patrick_star.keys()):
    print(f'{i+1} : {k}')

# parse the input from string to int
choice = int(input("Select a number:\n> "))

# get the actual key string
actualKey = list(patrick_star.keys())[choice - 1]

# print out the value
print(f"{patrick_star.get(actualKey, 'You must input a valid number!')}")