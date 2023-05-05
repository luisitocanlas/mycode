#!user/bin/env python3

# imports
import requests
import html
import json
from flask import Flask, redirect, url_for, request, render_template, jsonify

# represents the website
app = Flask(__name__)

# accessing API and storing them
gamedata = requests.get('https://www.moogleapi.com/api/v1/games').json()      


# landing or default page -----------------------------------------------------------------------
@app.route('/')
@app.route('/home')
def landingPage():
    return render_template('index.html')


# page for pure json ----------------------------------------------------------------------------
@app.route('/lezdoit', methods = ['POST', 'GET'])
def lezdoit():
    # fires when a post request happens
    if request.method == 'POST':
        data = request.json
        # get the data and append
        if data:
           data= json.loads(data)
           title = data["title"]
           picture = data["picture"]
           platform = data["platform"]
           releaseDate = data["releaseDate"]
           description = data["description"]
           gamedata.append({"title":title,"picture":picture,"platform":platform,"releaseDate":releaseDate,"description":description})
    # don't forget the jsonify and imports
    return jsonify(gamedata)


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
    # create a list with all the titles, used for game error handling
    titleList = []
    for game in gamedata:
        titleList.append(game['title'])

    if f'Final Fantasy {input}' in titleList:   # error handling
        for game in gamedata:
            if game['title'] == f'Final Fantasy {input}':
                ## returning list or json
                # return game

                ## using jinja2
                return render_template("game.html", game = game)
    else:
        return redirect('/home') # return to home if game is not in the data

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
    try:
        charList = []
  
        chardata = requests.get(f'https://www.moogleapi.com/api/v1/characters/search?name={input}').json()
    
        # loop through data
        for item in chardata:
            charDict = {}

            # put the desired data inside empty dictionary
            charDict['name'] = item['name']
            charDict['game'] = item['origin']
            charDict['description'] = html.unescape(item['description'])
            charDict['picture'] = item['pictures'][0]['url']

            # add the each dictionary to the list
            charList.append(charDict)

        ## returning list or json
        # return charList

        ## using jinja2
        return render_template("character.html", charlist = charList)

    except:
        return redirect('/home') # return to home if character doesn't exist


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2224, debug=True)
