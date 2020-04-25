# Contains all the code for the battle rooms
# Imports
from technical import text_type
import time, sys, points, opponent
import npc_system
from rock_paper_scissors import *

from technical import *

points.points_add()

def battle_room():
    
    print(f'You enter a room and see a {opponent.opponent}, they look at your menacingly.')
    battle_system.rock_paper_scissors()

    user_win_query()
    mission_continue()
    
    