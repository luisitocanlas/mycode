#!/usr/bin/python3

import requests
import os

NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    # with open("/home/student/mycode/nasa/nasa.creds", "r") as mycreds:
    #     nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    # nasacreds = "api_key=" + nasacreds.strip("\n")

    # more secure method, create environment API_KEY container
    apikey = os.getenv('API_KEY')
    nasacreds = 'api_key=' + apikey

    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## make a call to NASAAPI with our key
    apodresp = requests.get(NASAAPI + nasacreds)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
