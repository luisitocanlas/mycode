#!usr/bin/env python3

def main():
    num = int(input("How many bottles of beer do you want?\n> "))

    if num <= 100:
        for beer in range(num, 0, -1):
            print(f"{beer} bottles of beer on the wall!")
            print(f"{beer} bottles of beer on the wall! {beer} bottles of beer! You take one down, pass it around!")
    else:
        print("That's too many bottles of beer!")

if __name__ == "__main__":
    main()