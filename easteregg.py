# Imports
import sys, time, points, random

# Program
points.points_add()


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
    elif user_name.upper() == "69":
        text_type("Nice", 0.03)
    # Debug
    elif user_name.upper() == "DEBUG_POINTS":
        print("You get points")
        points.points += 100
    elif user_name.upper() == "DEBUG_WIN":
        print("You get points")
        points.points += 4999
        print(f"You now have {points.points} points")
        if points.points >= 5000:
            user_win()
            # print (f'===== You Win =====')
            # sys.exit()
    elif user_name.upper() == "DEBUG_RUN":
        print("Testing Exec")
        print("ONE")
        print("one")
        print(1)
        print(1.00)

        test_msg = "<---------->"
        for char in test_msg:
            time.sleep(0.5)
            sys.stdout.write(char)
            sys.stdout.flush()
        print("")
        print("test")
    elif user_name.upper() == 'DEBUG_RAND':
        rand_int = random.randint(1, 100)
        rand_int_two = random.randint(1, 50)
        rand_int_three = random.randint(1, 10)
        print(f"Rand_1: {rand_int}, Rand_2: {rand_int_two}, Rand_3: {rand_int_three}")
        time.sleep(1.5)
