# All the code for the randomly generated treasure rooms
# Import
from technical import text_type
import time, sys, points
points.points_add()

def tr_lobby():
    text_type("You step into a small chamber. It looks like a tiny reception hall.", 0.03)
    text_type("Just as you where about to move on you notice something sparkling in the corner.", 0.03)
    text_type("You pocket a small dagger.", 0.03)
    points.points += 5
    print(f'you now have {points.points} points')