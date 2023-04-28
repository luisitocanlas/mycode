#!usr/bin/env python3

#imports
import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

# container for the sliced trivia
sliced_trivia= {}

# slice function
def fix():
    for k,v in trivia.items():
        if isinstance(v, list):
            sliced_trivia[html.unescape(k)] = []
            for string in v:
                sliced_trivia[html.unescape(k)].append(html.unescape(string))
        else:
            sliced_trivia[html.unescape(k)] = html.unescape(v)

# print out the questions and choices
def show():
    print(sliced_trivia['question'])
    print(f"A) {sliced_trivia['correct_answer']}")
    print(f"B) {sliced_trivia['incorrect_answers'][0]}")
    print(f"C) {sliced_trivia['incorrect_answers'][1]}")
    print(f"D) {sliced_trivia['incorrect_answers'][2]}")

# ask the user for the answer
def ask():
    while True:
        ans = input("\n> ").upper().strip()
        if ans == "A":
            print("You guessed correctly!")
            break
        elif ans == "B" or ans == "C" or ans == "D":
            print("Sorry, please try again.")
            break
        else:
            print("Please select a valid letter.")

# main funciton
def main():
    fix()
    show()
    ask()

if __name__ == "__main__":
    main()
