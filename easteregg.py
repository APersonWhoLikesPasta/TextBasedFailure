import sys
import time

global points
points = 0

def user_death():
    print("")
    print("===== Game Over =====")
    print("")
    sys.exit()

def user_win():
    print("")
    print("===== You Win =====")
    print("")
    sys.exit()


def user_name_check(user_name):
    if user_name.upper() == "THANOS":
        print('A snap is heard, and you are turned to dust.')
        user_death()
    elif user_name.upper() == "EPIC GAMER":
        print('Ah, a true man of culture.')
        time.sleep(1.0)
        print("")
    elif user_name.upper() == "FINN":
        print("Oh. Well nevermind. We need compentent heros.")
        user_death()
    elif user_name.upper() == "CJ":
        user_win()
    elif user_name.upper() == "FRANKLIN":
        print(f"Congratulations you found some points, you now have {points}")
        