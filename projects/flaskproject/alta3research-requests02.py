#!/usr/bin/env python3
import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/lezdoit"

new_game = {
            "title" : "Final Fantasy Tactics",
            "picture" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGRO_lROd8S4URoitgo6pt3n5sukjYtUoapw&usqp=CAU",
            "platform" : "Sony Playstation",
            "releaseDate" : "June 20, 1997",
            "description" : "Final Fantasy Tactics is a strategy role-playing game in the Final Fantasy series. It was released for the PlayStation in June 1997, and has since been re-released as the updated Final Fantasy Tactics: The War of the Lions (ファイナルファンタジータクティクス 獅子戦争, Fainaru Fantajī Takutikusu Shishi Sensō?) for the PlayStation Portable, iOS and Android platforms. It was directed by Yasumi Matsuno and produced by Hironobu Sakaguchi, with Akihiko Yoshida providing the character designs and both Masaharu Iwata and Hitoshi Sakimoto providing the score. It was the first strategy role-playing game in the series. The game is set in Ivalice, a unified kingdom of seven territories, which is caught in the middle of the War of the Lions fought between two opposing factions vying for rule of the kingdom. The story focuses on Ramza Beoulve, a member of the respected House Beoulve, who finds himself caught amid the war and later uncovers the truth behind a sinister plot behind it. Final Fantasy Tactics features battles fought on a map divided into a grid in which units can move. The order of units' turns is determined by an 'Active-Time' like system, and actions can only be executed within a range of the units' position. Units each have a job class which provides them abilities, but they can also equip abilities from other jobs they have leveled up or mastered. Final Fantasy Tactics is the first game set in the recurring setting of Ivalice, which was later the setting of main series installment Final Fantasy XII. It has also spawned spinoffs Final Fantasy Tactics Advance and Final Fantasy Tactics A2: Grimoire of the Rift. Games that take place in Ivalice have later been grouped in the Ivalice Alliance series."
            }

# convert to json string
new_game = json.dumps(new_game)

# send a POST request
updated_games = requests.post(URL, json=new_game)

# pretty-print the response back from our POST request
pprint(updated_games.json())