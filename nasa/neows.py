#!/usr/bin/python3
import requests
import pprint
import os
from dotenv import load_dotenv

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    # with open("/home/student/nasa.creds", "r") as mycreds:
    #     nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    # nasacreds = "api_key=" + nasacreds.strip("\n")

    # more secure method, API_KEY defined in environment
    apikey = os.getenv('API_KEY')
    nasacreds = 'api_key=' + apikey

    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    # startdate = "start_date=2019-11-11"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    ## custom 01
    ## ask user for date
    userstartdate = input('Enter a start date (YYYY-MM-DD):\n> ')
    startdate = f'start_date={userstartdate}'

    userenddate = input('(OPTIONAL) Enter an end date (YYYY-MM-DD):\n> ')
    if userenddate == '':
        enddate = ''
    else:
        enddate = f'&end_date={userenddate}'

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + enddate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)


if __name__ == "__main__":
    main()
