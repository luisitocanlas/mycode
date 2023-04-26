#!usr/bin/env python3
import random

wordbank= ["indentation", "spaces"] 

tlgstudents= ["Brandon", "Caleb", "Cat", "Chad the Beardulous", "Chance", "Chris", "Jessica", "Jorge", "Joshua", "Justin", "Lui", "Stephen"]

def main():
    # add 4 to the wordbank
    wordbank.append(4)

    # get a number to use for splicing
    #  num = int(input("Give me a number between 0 and 11: "))
    num = random.randint(0, 11)

    # get the student using num
    student_name = tlgstudents[num]



    # print out using the student and wordbank
    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

main()
