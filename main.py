###################################################################
#                A Text Based Adventure Game                      #
# ----------------------------------------------------------------#
#                        Micro-README                             #
# ----------------------------------------------------------------#
# This is a test based adventure game. To keep things clean and   #
# organized there are certain standards which you must adhere to. #
# All standards are in the README. Read it. Failure to adhere to  #
# these standards will result in messy code. Please adhere to any #
# and all standards.                                              #
###################################################################

# Imports
import time, sys, easteregg, points, rand_room
from technical import *
# Rooms
from treasure_room import *
from rock_paper_scissors import *

# Variables
intro = open('intro.txt')
contributors = open('contributors.txt')
global user_name
user_name = ""
points.points_add()


# Debug Functions


###########
# Program #
###########

# User
def user_tutorial():
    while True:
        text_type(
            """
Greetings! In this game you will face many difficult decisions. When you are asked 
for a response you must answer with the capitalized option. \nDo you UNDERSTAND?
""", 0.03)
        understanding = input('> ')
        if understanding.upper() == "UNDERSTAND":
            break
        else:
            continue
    text_type("Fantastic\n", 0.03)
    time.sleep(0.5)


def user_name_selection():
    text_type("What is your name?", 0.03)
    user_name = input('> ')
    easteregg.user_name_check(user_name)
    text_type(f'Glad to have you {user_name}!', 0.03)


def mission_brief():
    text_type("You are a wealthy g̶r̶a̶v̶e̶ ̶r̶o̶b̶b̶e̶r̶, archeologist.", 0.03)
    text_type("You are in search of secret artifacts.", 0.03)
    text_type("Each artifact you collect will give you a varying amount of points.", 0.03)
    text_type("==========", 0.03)
    time.sleep(0.5)


def mission_start():
    text_type(
        "You slowly approach the entrance. As you get closer you think that devs should have \nmade this more "
        "interesting, but when you remember that the devs can't write themselves out of a bag. \nOr spell for that."
        "matter",
        0.03)
    text_type("You duck inside.", 0.03)


# User End
def user_dead():
    print("")
    print("===== Game Over =====")
    print("")
    sys.exit()


def user_win():
    print("===== You Win =====")
    sys.exit()


# Exec
if __name__ == "__main__":
    # Debug    
    # dry_run(0.5)

    # Title Screen
    text_type(intro, 0.1)
    text_type(contributors, 0.1)
    # Intro
    user_tutorial()
    user_name_selection()
    # Mission
    mission_brief()
    mission_start()
    # rock_paper_scissors.rock_paper_scissors()
    while points.points <= 500000:
        rand_room.room_select_begin()
else:
    print("Please run this module directly")
    sys.exit()
