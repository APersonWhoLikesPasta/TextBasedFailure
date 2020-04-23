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

# Variables
intro = open('intro.txt')
contributors = open('contributors.txt')

# Debug Functions
def dry_run():
    print("Testing Exec")
    print("ONE")
    print("one")
    print(1)
    print(1.0)

# Program
def text_type(msg, speed):
    for char in msg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()

# Exec
if __name__ == "__main__":
    # Debug    
    #dry_run()

    # Intro
    text_type(intro, 0.1)
    text_type(contributors, 0.1)
