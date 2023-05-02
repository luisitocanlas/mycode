#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

# create a function that looks through the links
def getData(data):
    dataList = []
    for url in data:
        rawData = requests.get(url)
        formattedData = rawData.json()
        dataList.append(formattedData['name'])
    return dataList

def main():
    ## Ask user for input
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! ")

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    # pprint.pprint(got_dj)
    
    # look up character
    char = got_dj['name']
    print(f'Name: {char}')

    # return house(s) affiliated
    houseList = getData(got_dj['allegiances'])
    print(f'House(s) affiliated: {houseList}')
    
    # return list of book appearances
    bookList = getData(got_dj['books'])
    print(f'Book appearances: {bookList}')
  

if __name__ == "__main__":
    main()
