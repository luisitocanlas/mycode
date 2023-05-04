#!usr/bin/env python3

# imports
import requests
import pprint
import html

# apiUrl = 'https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple'

def userInput():
    # show categories
    categories = requests.get('https://opentdb.com/api_category.php').json()
    for category in categories['trivia_categories']:
        print(f'{category["id"]}) {category["name"]}')
    cat = input('Select a number from the list of categories above:\n> ')

    # get difficulty
    print('Select difficulty:')
    print('1. Easy')
    print('2. Medium')
    print('3. Hard')
    ans2 = input('> ')
    if ans2 == '1':
        dif = 'easy'
    elif ans2 == '2':
        dif = 'medium'
    elif ans2 == '3':
        dif = 'hard'

    # get type
    que = ''
    print('Select type:')
    print('1. Multiple Choice')
    print('2. True / False')
    ans3 = input('> ')
    if ans3 == '1':
        que = 'multiple'
    elif ans3 == '2':
        que = 'boolean'

    # return the url
    return f'https://opentdb.com/api.php?amount=10&category={cat}&difficulty={dif}&type={que}'

def showQA(data):
    #show question
    q = 0
    for que in data['results']:
        q += 1
        cQue = html.unescape(que['question'])
        print(f'{q}) {cQue}')

        # get answers and sort, maybe change the sort to a list randomizer
        ansList = [que['correct_answer']]
        for ans in que['incorrect_answers']:
            ansList.append(ans)
        ansList.sort()

        # show answers
        n = 0
        for a in ansList:
            n += 1
            print(f'\t{n}) {a}')

        print('')   # just a breakline
        

def main():
    # ask user for input
    apiUrl = userInput()

    # send GET request and apply json method
    data = requests.get(apiUrl).json()

    # show data
    showQA(data)


if __name__ == '__main__':
    main()