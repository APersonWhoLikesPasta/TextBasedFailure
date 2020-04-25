# Imports
import sys
import time
import points
from technical import *

def text_type(msg, speed):
    for char in msg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")


def debug_end():
    print("===== Game Ended =====")
    sys.exit()


def mission_continue():
    
    
    while True:
        text_type("\n===== Press an WASD to Choose your Direction =====", 0.03)
        Movementinput = input('> ')

        if Movementinput.upper() == 'W':
            text_type("You advance to the next room.", 0.03)
            text_type("==========", 0.03)
            break
        elif Movementinput.upper() == 'A':
            text_type("You advance to the next room.", 0.03)
            text_type("==========", 0.03)
            break
        elif Movementinput.upper() == 'S':
            text_type("You advance to the next room.", 0.03)
            text_type("==========", 0.03)
            break
        elif Movementinput.upper() == 'D':
            text_type("You advance to the next room.", 0.03)
            text_type("==========", 0.03)
            break
        else:
            continue


def user_win_query(): # This one counts
    if points.points >= 3000:
        print("===== You Win =====")
        sys.exit()