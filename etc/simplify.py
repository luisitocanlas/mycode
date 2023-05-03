#!/usr/bin/env python3

zodiac = {
    0:'Your zodiac sign is Monkey, you are sharp, smart, curious, and mischievious.',
    1:'Your zodiac sign is Rooster, you are hardworking, resourceful, courageous, and talented.',
    2:'Your zodiac sign is Dog, you are loyal, honest, cautious, and kind.',
    3:'Your zodiac sign is Pig, you are a symbol of wealth, honesty, and practicality.',
    4:'Your zodiac sign is Rat, you are artistic, sociable, industrious, charming, and intelligent.',
    5:'Your zodiac sign is Ox, you are strong, thorough, determined, loyal, and reliable.',
    6:'Your zodiac sign is Tiger, you are courageous, enthusiastic, confident, charismatic, and a leader.',
    7:'Your zodiac sign is Rabbit, you are vigilant, witty, quick-minded, and ingenious.',
    8:'Your zodiac sign is Dragon, you are talented, powerful, lucky, and successfull.',
    9:'Your zodiac sign is Snake, you are wise, like to work alone, and determined.',
    10:'Your zodiac sign is Horse, you are animated, active, and energetic.',
    11:'Your zodiac sign is Goat, you are creative, resilient, gentle, mild-mannered, and shy.'
}

def main():    
    try:
        # get user name
        usr_name = input("Please enter your name:\n> ") 
        usr_name = usr_name.title()    

        # get birth date
        usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n> "))
        x = usr_date % 12

        print(f'Hi {usr_name}! {zodiac[x]}')

    except:
        print('Error: computer cannot compute...')
 
if __name__ == "__main__":
    main()