#!usr/bin/env python3

print("Which Gundam Should You Pilot?\n")

print("Welcome to the world of Gundam! With so many different mobile suits to choose from, it can be tough to decide which one is right for you. Take this quiz to find out which Gundam you should be piloting.\n")

# dictionary for counting up answers
answers = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
}

# Question 1
print("What's your preferred combat style?")
print("a) Close-range melee combat")
print("b) Long-range sniping")
print("c) Balanced all-around combat")
print("d) Strategic support and defense\n")

# loop until you get a, b, c, d as an answer
while True:
    ans = input("Select your answer:\n> ").lower().strip()
    print("") # just a line break
    if ans == "a":
        answers["a"] += 1
        break
    elif ans == "b":
        answers["b"] += 1
        break
    elif ans == "c":
        answers["c"] += 1
        break
    elif ans == "d":
        answers["d"] += 1
        break
    else:
        print("Invalid input. Please try again.")

# Question 2
print("How do you prefer to handle difficult situations?")
print("a) Head on, with brute force")
print("b) With precision and calculated moves")
print("c) With a mix of quick thinking and improvisation")
print("d) With defensive tactics and protection\n")

# loop until you get a, b, c, d as an answer
while True:
    ans = input("Select your answer:\n> ").lower().strip()
    print("") # just a line break
    if ans == "a":
        answers["a"] += 1
        break
    elif ans == "b":
        answers["b"] += 1
        break
    elif ans == "c":
        answers["c"] += 1
        break
    elif ans == "d":
        answers["d"] += 1
        break
    else:
        print("Invalid input. Please try again.")

# Question 3
print("How important is teamwork to you?")
print("a) Not important, I work best on my own")
print("b) I can work with a partner if needed, but prefer to be solo")
print("c) Teamwork is essential, but I can lead if needed")
print("d) I thrive in a team environment and enjoy being a supportive member\n")

# loop until you get a, b, c, d as an answer
while True:
    ans = input("Select your answer:\n> ").lower().strip()
    print("") # just a line break
    if ans == "a":
        answers["a"] += 1
        break
    elif ans == "b":
        answers["b"] += 1
        break
    elif ans == "c":
        answers["c"] += 1
        break
    elif ans == "d":
        answers["d"] += 1
        break
    else:
        print("Invalid input. Please try again.")

# Question 4
print("What's your preferred environment to operate in?")
print("a) Urban areas and cities")
print("b) Open fields and natural landscapes")
print("c) Space and zero-gravity environments")
print("d) Anywhere with plenty of cover and defense options\n")

# loop until you get a, b, c, d as an answer
while True:
    ans = input("Select your answer:\n> ").lower().strip()
    print("") # just a line break
    if ans == "a":
        answers["a"] += 1
        break
    elif ans == "b":
        answers["b"] += 1
        break
    elif ans == "c":
        answers["c"] += 1
        break
    elif ans == "d":
        answers["d"] += 1
        break
    else:
        print("Invalid input. Please try again.")

# Question 5
print("How important is speed and agility to you?")
print("a) Very important, I need to be able to move quickly and dodge attacks")
print("b) Somewhat important, but I prefer to focus on defense")
print("c) Not important, I prefer to be a heavy hitter")
print("d) Moderately important, I need to be able to maneuver in tight spaces\n")

# loop until you get a, b, c, d as an answer
while True:
    ans = input("Select your answer:\n> ").lower().strip()
    print("") # just a line break
    if ans == "a":
        answers["a"] += 1
        break
    elif ans == "b":
        answers["b"] += 1
        break
    elif ans == "c":
        answers["c"] += 1
        break
    elif ans == "d":
        answers["d"] += 1
        break
    else:
        print("Invalid input. Please try again.")

# Question 6
print("What's your preferred weapon of choice?")
print("a) A melee weapon like a sword or axe")
print("b) A long-range weapon like a sniper rifle or beam rifle")
print("c) A combination of both melee and ranged weapons")
print("d) Defensive weapons like shields or beam sabers\n")

# loop until you get a, b, c, d as an answer
while True:
    ans = input("Select your answer:\n> ").lower().strip()
    print("") # just a line break
    if ans == "a":
        answers["a"] += 1
        break
    elif ans == "b":
        answers["b"] += 1
        break
    elif ans == "c":
        answers["c"] += 1
        break
    elif ans == "d":
        answers["d"] += 1
        break
    else:
        print("Invalid input. Please try again.")

# Question 7
print("What motivates you to fight?")
print("a) Personal glory and recognition")
print("b) A desire to protect others and maintain peace")
print("c) Revenge or a desire to get even with enemies")
print("d) A sense of duty and responsibility to others\n")

# loop until you get a, b, c, d as an answer
while True:
    ans = input("Select your answer:\n> ").lower().strip()
    print("") # just a line break
    if ans == "a":
        answers["a"] += 1
        break
    elif ans == "b":
        answers["b"] += 1
        break
    elif ans == "c":
        answers["c"] += 1
        break
    elif ans == "d":
        answers["d"] += 1
        break
    else:
        print("Invalid input. Please try again.")

# print out answers
print(answers)

# Give the user their Gundam!
if answers["a"] >= 4:
    print("Gundam Barbatos (Mobile Suit Gundam Iron-Blooded Orphans).\nYou're a close-range  pilot who relies on brute force to get the job done. The Gundam Barbatos is the perfect match for your combat style, with its powerful melee weapons and heavy armor that can take a beating. As a pilot of the Barbatos, you'll be a fearsome force on the battlefield, striking fear into the hearts of your enemies with each swing of your weapon.")
elif answers["b"] >= 4:
    print("Gundam Dynames (Mobile Suit Gundam 00)\nYou're a precise and calculated  pilot who prefers to take out enemies from afar. The Gundam Dynames is the perfect match for your combat style, with its long-range sniper rifle and precision targeting system that can take out enemies from a safe distance. As a pilot of the Dynames, you'll be a deadly assassin on the battlefield, picking off enemies one by one with your expert marksmanship.")
elif answers["c"] >= 4:
    print("Gundam Strike Freedom (Mobile Suit Gundam Seed Destiny)\nYou're a well-rounded  pilot who can hold your own in any situation. The Gundam Strike Freedom is the perfect match for your combat style, with its combination of melee and ranged weapons that can handle any situation. As a pilot of the Strike Freedom, you'll be a versatile and powerful force on the battlefield, able to take on any challenge that comes your way.")
elif answers["d"] >= 4:
    print("Gundam Heavyarms Custom (Mobile Suit Gundam Wing)\nYou're a heavy weapons specialist who prefers to overwhelm your opponents with sheer firepower. The Gundam Heavyarms Custom is the perfect match for your combat style, with its array of heavy machine guns, missiles, and other devastating weapons. As a pilot of the Heavyarms Custom, you'll be a force to be reckoned with on the battlefield, raining down a hail of bullets and missiles on your enemies that they won't soon forget.")
elif answers["a"] >= 3 and answers["b"] >= 3:
    print("Gundam Kyrios (Mobile Suit Gundam 00)\nYou're a versatile  pilot who can adapt to any situation. The Gundam Kyrios is the perfect match for your combat style, with its ability to transform into different modes and its array of powerful weapons. As a pilot of the Kyrios, you'll be a jack-of-all-trades on the battlefield, able to handle any challenge that comes your way. With its advanced systems and the ability to transform into a fighter jet, you'll be able to outmaneuver and outgun your opponents with ease.")
elif answers["a"] >= 3 and answers["c"] >= 3:
    print("Gundam Exia (Mobile Suit Gundam 00)\nYou're a well-rounded  pilot with a strong sense of justice. The Gundam Exia is the perfect match for your combat style, with its combination of speed, agility, and powerful weapons. As a pilot of the Exia, you'll be a heroic figure on the battlefield, fighting for what's right and taking down your enemies with swift and decisive strikes.")
elif answers["a"] >= 3 and answers["d"] >= 3:
    print("Gundam Sandrock (Mobile Suit Gundam Wing)\nYou're a  pilot who prefers a straightforward approach to combat. The Gundam Sandrock is the perfect match for your combat style, with its heavy armor and powerful heat weapons. As a pilot of the Sandrock, you'll be a dependable presence on the battlefield, able to take on multiple enemies at once with ease. With its powerful heat shotels and advanced systems, you'll be able to cut through enemy lines and emerge victorious.")
elif answers["b"] >= 3 and answers["c"] >= 3:
    print("Gundam Deathscythe (Mobile Suit Gundam Wing)\nYou're a  pilot who prefers a stealthy approach to combat. The Gundam Deathscythe is the perfect match for your combat style, with its ability to cloak and its array of powerful weapons. As a pilot of the Deathscythe, you'll be able to take out enemies from the shadows and strike fear into the hearts of your opponents. With its powerful beam scythe and advanced systems, you'll be a force to be reckoned with on the battlefield.")
elif answers["b"] >= 3 and answers["d"] >= 3:
    print("Gundam Virtue (Mobile Suit Gundam 00)\nYou're a strategic  pilot who prefers a defensive approach to combat. The Gundam Virtue is the perfect match for your combat style, with its heavy armor and powerful weapons that can take on any challenge. As a pilot of the Virtue, you'll be a stalwart defender on the battlefield, providing cover and support to your allies and taking down your enemies with powerful beam attacks. With its advanced Nadleeh System and ability to transform into a sleeker form, you'll be able to adapt to any situation and emerge victorious.")
elif answers["c"] >= 3 and answers["d"] >= 3:
    print("Gundam Unicorn (Mobile Suit Gundam Unicorn)\nYou're a  pilot with a strong sense of justice and a desire to protect those around you. The Gundam Unicorn is the perfect match for your combat style, with its advanced systems and powerful weapons. As a pilot of the Unicorn, you'll be able to unleash devastating attacks with its beam magnum and destroy your enemies with its psychoframe system. With the Gundam Unicorn by your side, you'll be able to fight for what's right and protect those in need.")
elif answers["a"] == 2 and answers["b"] == 2 and answers["c"] >= 2:
    print("Zeta Gundam (Mobile Suit Zeta Gundam)\nYou're a pilot who values both speed and precision in combat. The Gundam Zeta is a perfect match for your style, with its advanced mobility and superior weaponry. As a pilot of the Zeta, you'll be able to outmaneuver and outgun your opponents, using its powerful beam saber and beam rifle in close combat, and its powerful Mega Particle Cannon for long-range attacks. The Zeta's transforming ability also gives it unmatched agility, allowing you to quickly switch between its Mobile Suit and Wave Rider forms depending on the situation. With its advanced technology and your piloting skills, you'll be able to take on any enemy and emerge victorious. But be careful, as the Zeta is a highly advanced machine and requires a skilled and experienced pilot to fully unleash its true potential.")
elif answers["a"] >= 2 and answers["b"] == 2 and answers["d"] == 2:
    print("Gundam Epyon (Mobile Suit Gundam Wing)\nYou're a  pilot who values speed and precision in combat. The Gundam Epyon is the perfect match for your combat style, with its incredible speed and deadly melee weapons. As a pilot of the Epyon, you'll be able to dart around the battlefield with ease, using its beam sword and heat rod to slice through your enemies like butter. With its powerful thrusters and advanced systems, the Epyon can also outmaneuver and outgun its opponents with ease, making it a formidable Gundam in any situation. With the Gundam Epyon by your side, you'll be a force to be reckoned with on the battlefield, striking fear into the hearts of your enemies with every swing of your beam sword.")
elif answers["a"] == 2 and answers["c"] == 2 and answers["d"] >= 2:
    print("Gundam Nadleeh (Mobile Suit Gundam 00)\nYou're a  pilot who values versatility and adaptability in combat. The Gundam Nadleeh is the perfect match for your combat style, with its unique ability to transform into the GN-009 Seraphim Gundam for stealth and reconnaissance missions. As a pilot of the Nadleeh, you'll be able to switch between forms depending on the situation, using its powerful GN Beam Saber and GN Beam Rifle to take down your enemies. The Nadleeh's Trans-Am system also gives it a boost of speed and power when needed, allowing you to overwhelm your foes in an instant. With its advanced sensor systems and tactical abilities, the Nadleeh can also analyze enemy movements and react accordingly, making it a formidable Gundam in any situation. With the Gundam Nadleeh by your side, you'll be a master of versatility and adaptability, able to handle any mission that comes your way with ease and emerge victorious on the battlefield.")
elif answers["b"] == 2 and answers["c"] >= 2 and answers["d"] == 2:
    print("Gundam Aegis (Mobile Suit Gundam SEED)\nYou're a  pilot who values strategy and cunning in combat. The Gundam Aegis is the perfect match for your combat style, with its advanced transformation system and versatile arsenal. As a pilot of the Aegis, you'll be able to transform between its two forms - mobile suit and flight mode - to adapt to any situation on the battlefield. The Aegis is also equipped with powerful beam weapons, including its signature beam sabers and its high-output beam rifle, which can penetrate even the thickest armor. Its Mirage Colloid stealth system also allows it to become invisible to the naked eye, making it an ideal choice for covert operations. With its advanced systems and versatile weaponry, the Gundam Aegis is a formidable opponent on the battlefield, able to outmaneuver and outsmart even the most skilled enemy pilots. With the Aegis by your side, you'll be a master strategist, able to turn the tide of battle in your favor with clever tactics and precise attacks.")
else:
    print("Gundam Wing Zero (Mobile Suit Gundam Wing)\nCongratulations, you are the perfect match for the Gundam Wing Zero! As a pilot of this powerful mobile suit, you possess a balanced skill set and the ability to adapt to any situation. The Wing Zero's advanced weaponry and mobility allow for both long-range attacks and close combat, making it a versatile and formidable force on the battlefield. Your piloting skills will be put to the test as you navigate through challenging battles, but with the Gundam Wing Zero by your side, you're sure to emerge victorious. Good luck, pilot!")
