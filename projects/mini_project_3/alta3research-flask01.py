#!user/bin/env python3

# imports
import requests
import html
from flask import Flask, redirect, url_for, request, render_template

# represents the website
app = Flask(__name__)
        
# landing or default page
@app.route('/')
@app.route('/home')
def landingPage():
    return render_template('index.html')

# if the user click on get game -----------------------------------------------------------------
# get the user input for game
@app.route('/game', methods=['POST'])
def choosegame():
    if request.form['game']:
        value = request.form['game'] # store the value
    else:
        value = '06' # default value

    return redirect(url_for('resultgame', input = value))

# show the game result
@app.route('/resultgame/<input>')
def resultgame(input):
    data = requests.get('https://www.moogleapi.com/api/v1/games').json()
    
    for game in data:
        if game['title'] == f'Final Fantasy {input}':
            # returning json
            # return game
            
            # using jinja2
            return render_template("game.html", game = game)
    

# if the user click on get character ------------------------------------------------------------
# get the user input for character
@app.route('/character', methods=['POST'])
def choosechar():
    if request.form['character']:
        value = request.form['character'] # store the value
    else:
        value = 'Mog' # return default value

    return redirect(url_for('resultchar', input = value))

# show the character results
@app.route('/resultchar/<input>')
def resultchar(input):
    charList = []
  
    data = requests.get(f'https://www.moogleapi.com/api/v1/characters/search?name={input}').json()
    
    # loop through data
    for item in data:
        charDict = {}

        # put the desired data inside empty dictionary
        charDict['name'] = item['name']
        charDict['game'] = item['origin']
        charDict['description'] = html.unescape(item['description'])
        charDict['picture'] = item['pictures'][0]['url']

        # add the each dictionary to the list
        charList.append(charDict)

    # print(charList)
    # return charList

    # using jinja2
    return render_template("character.html", charlist = charList)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224, debug=True)
