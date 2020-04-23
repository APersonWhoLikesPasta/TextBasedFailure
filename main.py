###############################
# A Text Based Adventure Game #
###############################
#        Contributers         #
#-----------------------------#
# Franklin                    #
#                             #
###############################
#         Micro-README        #
#-----------------------------#####################################
# This is a test based adventure game. To keep things clean and   #
# organized there are certain standards which you must adhere to. #
# All standards are in the README. Read it. Failure to adhere to  #
# these standards will result in messy code. Please adhere to any #
# and all standards.                                              #
###################################################################

# Imports
import time
import sys
from easteregg import user_name_check

# Variables
intro = open('intro.txt')
contributors = open('contributors.txt')
global user_name
user_name = ""

# Debug Functions
def dry_run():
    print("Testing Exec")
    print("ONE")
    print("one")
    print(1)
    print(1.0)


def text_type_test(speed):
    msg = "<----------> \n"
    for char in msg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

###########
# Program #
###########

# User
def user_tutorial():
    while True:
        print(
"""
Greetings! In this game you will face many diffucult decions. When you are asked for a respounce
you must answer with the capitlized option. Do you UNDERSTAND?
""")
        understanding = input('> ')
        if understanding.upper() == "UNDERSTAND":
            break
        else:
            continue
    print("Fantastic \n")


def user_class_selection():
    print("What is your name?")
    user_name = input('> ')
    #from easteregg import user_name_check
    user_name_check(user_name)
    print(f"Glad to have you {user_name}!") # Nothing is wrong. I tried on my comp.


def user_dead():
    print("")
    print("===== Game Over =====")
    print("")
    sys.exit()


# Miscellanous
def text_type(msg, speed):
    for char in msg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()


# Exec
if __name__ == "__main__":
    # Debug    
    #dry_run()
    #text_type_test(0.09)

    # Intro
    text_type(intro, 0.1)
    text_type(contributors, 0.1)

    user_tutorial()
    user_class_selection()

else:
    print("Please run this module directly")
    quit()
