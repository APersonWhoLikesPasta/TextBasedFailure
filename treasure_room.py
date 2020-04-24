# All the code for the randomly generated treasure rooms
# Import
from technical import text_type
import time, sys, points
from random import randint
points.points_add()


def tr_lobby():
    text_type("You step into a small chamber. It looks like a tiny reception hall.", 0.03)
    text_type("Just as you where about to move on you notice something sparkling in the corner.", 0.03)
    treasure = randint(1, 3)
    if treasure == 1:
        text_type("You find a small dagger.", 0.03)
    elif treasure == 2:
        text_type("You find a small dagaer with a skull embosed on on the crossguard.", 0.03)
    elif treasure == 3:
        text_type("You find a small dagger embossed with a skull.", 0.03)
    else:
        print("ERROR: Help! `treasure_room.py` isn't working! HELP!")
        while True:
            text_type("HELP!",0.03)
            text_type("HELP ME!", 0.03)
            text_type("Theres been an ERROR!", 0.03)
    points.points += 5
    print(f'you now have {points.points} points')   
    if points.points >= 5000:
        print (f'===== You Win =====')
        sys.exit()