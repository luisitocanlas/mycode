#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # the player known as the swapper
    # swapper = Cheat_Swapper()
    # the player known as the loaded_dice
    # loaded_dice = Cheat_Loaded_Dice()
    cheater1 = Cheat_Fifty()
    cheater2 = Cheat_Sabotage()
    

    # track scores for both players
    # swapper_score = 0
    # loaded_dice_score = 0
    cheater1_score = 0
    cheater2_score = 0


    # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        cheater1.roll()
        cheater2.roll()

        cheater1.cheat()
        cheater2.cheat(cheater1)
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(cheater1.get_dice()) == sum(cheater2.get_dice()):
            #print("Draw!")
            pass
        elif sum(cheater1.get_dice()) > sum(cheater2.get_dice()):
            #print("Dice swapper wins!")
            cheater1_score+= 1
        else:
            #print("Loaded dice wins!")
            cheater2_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Cheater 1 won: {cheater1_score}")
    print(f"Cheater 2 won: {cheater2_score}")

    # determine the winner
    if cheater1_score == cheater2_score:
        print("Game was drawn")
    elif cheater1_score > cheater2_score:
        print("Cheater 1 won most games")
    else:
        print("Cheater 2 won most games")

if __name__ == "__main__":
    main()
