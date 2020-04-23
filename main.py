###############################
# A Text Based Adventure Game #
###############################
#        Contributers         #
#-----------------------------#
# Franklin                    #
# CJ                          #
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
import easteregg
import test

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
    print(1.00
    
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
        text_type(
"""
Greetings! In this game you will face many diffucult decions. When you are asked for a respounce
you must answer with the capitlized option. \nDo you UNDERSTAND?
""", 0.05)
        understanding = input('> ')
        if understanding.upper() == "UNDERSTAND":
            break
        else:
            continue
    print("Fantastic \n")


def user_name_selection():
    print("What is your name?")
    user_name = input('> ')
    easteregg.user_name_check(user_name)
    print(f'Glad to have you {user_name}!')


# User End
def user_dead():
    print("")
    print("===== Game Over =====")
    print("")
    sys.exit()

def user_win():
    print("===== You Win =====")
    sys.exit()


# Technical
def text_type(msg, speed):
    for char in msg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()


# Exec
if __name__ == "__main__":
    # Debug    
    #dry_run()

    # Titlescreen
    text_type(intro, 0.1)
    text_type(contributors, 0.1)
    # Intro
    user_tutorial()
    user_name_selection()

else:
    print("Please run this module directly")
    quit()
