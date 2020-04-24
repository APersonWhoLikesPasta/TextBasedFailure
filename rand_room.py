# Imports
import sys
import time
import points
import random
from technical import *

#Room Imports
from misc_room import *
from treasure_room import *
from battle_room import *

points.points_add()

def room_select_begin():
    room_select_begin = random.randint(1, 3)
    if room_select_begin == 1:
        tr_lobby()
    elif room_select_begin == 2:
        misc_room()
    elif room_select_begin == 3:
        battle_room()
    else:
        print(room_select_begin)