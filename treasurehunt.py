"""tarting Point:

The player is welcomed and given their mission to find the treasure.

First Choice:

The player is at a crossroads and must choose to go "left" or "right".

Choosing "right" results in falling into a hole and ending the game.

Second Choice:

Upon choosing "left", the player reaches a lake and decides whether to "wait" for a boat or "swim" across.

Swimming results in being attacked by trout and ending the game.

Third Choice:

Waiting for the boat successfully takes the player to an island with three colored doors (red, yellow, blue).

Choosing the "yellow" door leads to the treasure and winning the game.

Choosing the "red" door leads to a room full of fire, and the "blue" door leads to a room of beasts, both ending the game."""

a="""*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/_____/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************"""
print(a)
print("welcome to treasure island")
print("your mission is to find the treasure")
c=input("you are at a crossroads, do you want to go left or right?")
if c=="left" or c=="LEFT":
    c1=input("you have reached a lake, do you want to wait for a boat or swim across the lake").lower()
    if c1=="boat":
        c2=input("you have reached an island with three colored doors, do you want to choose which color red blue green")
        if c2=="red":
            print("red door leads to a room full of fire u are dead")
        elif c2=="blue":
            print("blue door leads to a room of beasts u are dead")
        elif c2=="yellow":
            print("u find the treasure u are win")
    else:
        print("u are attacked by trout and ending the game.")

else :
    print("you have fallen into a hole and died")
