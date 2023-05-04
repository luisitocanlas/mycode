#!user/bin/env python3

# imports
import requests
from flask import Flask, redirect, url_for, request, render_template

# URLs
# ffChars = 'https://www.moogleapi.com/api/v1/characters'
# chars = requests.get(ffChars).json()

# represents the website
app = Flask(__name__)
        
# landing or default page
@app.route('/')
@app.route('/home')
def landingPage():
    return render_template('index.html')

# get the user input
@app.route('/choice', methods=['POST'])
def choose():
    if request.form['chosen']:
        value = request.form['chosen'] # store the value
    else:
        value = 'Mog' # return default value

    return redirect(url_for('result', input = value))

# show the user results
@app.route('/result/<input>')
def result(input):
    charList = []
  
    data = requests.get(f'https://www.moogleapi.com/api/v1/characters/search?name={input}').json()
    
    # loop through data
    for item in data:
        charDict = {}

        # put the desired data inside empty dictionary
        charDict['name'] = item['name']
        charDict['game'] = item['origin']
        charDict['description'] = item['description']

        # add the each dictionary to the list
        charList.append(charDict)

    # print(charList)
    return charList


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224, debug=True)
