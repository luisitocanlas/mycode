#!usr/bin/env python3

# farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
#          {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
#          {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]

animals = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

# show farms
def showFarm():
    print("Select a farm from the following:")
    for idx, farm in enumerate(farms):
        print(f"{idx+1}) {farm['name']}")

# user selects farm
def chooseFarm():
    # TODO implement user error handling
    while True:
        try:
            userFarm = int(input("> "))
            if 1 <= userFarm <= len(farms):
                for idx, farm in enumerate(farms):
                    if idx+1 == userFarm:
                        return farm
                        break
            else:
                print("Invalid input")
        except:
            print("Invalid input")

# return animals from farm
def returnAnimals(farm):
    for animal in farm['agriculture']:
        if animal in animals:
            print(animal)

def main():
    showFarm()
    selectedFarm = chooseFarm()
    returnAnimals(selectedFarm)
    
if __name__ == "__main__":
    main()