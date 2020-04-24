# imports
import time
import sys


def text_type(msg, speed):
    for char in msg:
        time.sleep(speed)
        sys.stdout.write(char)
        sys.stdout.flush()
    print("")

def debug_end():
    print("===== Game Ended =====")
    sys.exit()
