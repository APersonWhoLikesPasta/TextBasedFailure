from random import randint
import points, opponent
from technical import *


points.points_add()

def rock_paper_scissors():
    text_type("You have three attacks. You can LUNGE, PUCNH, or STAB.", 0.03)
    Playerinput = input ()
    Gameinput = randint (1, 3)
    print (Gameinput)
    if Gameinput == 1:
        if Playerinput == ('STAB'):
            print(f'The {opponent.opponent} dodged your attack.')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')
    if Gameinput == 1:
        if Playerinput == ('LUNGE'):
            print ('Your a Loser')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')
    if Gameinput == 1:
        if Playerinput == ('PUNCH'):
            points.points += 100
            print(f'Go Get em! You Win, and now have {points.points} points')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')

    if Gameinput == LUNGE:
        if Playerinput == ('LUNGE'):
            print(f'The {opponent.opponent} dodged your attack.')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')
    if Gameinput == LUNGE:
        if Playerinput == ('PUNCH'):
            print('I knew you were a faliure when you first touched the keyboard')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')
    if Gameinput == LUNGE:
        if Playerinput == ('STAB'):
            points.points += 100
            print(f'Winner Winner Chicken Dinner, you now have {points.points} points')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')

    if Gameinput == PUNCH:
        if Playerinput == ('PUNCH'):
            print(f'The {opponent.opponent} dodged your attack.')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')
    if Gameinput == PUNCH:
        if Playerinput == ('STAB'):
            print("You died a horrible death, and made {opponent.opponent} very happy.")
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')
    if Gameinput == 2:
        if Playerinput == ('LUNGE'):
            points.points += 100
            print(f'You Win! You now have {points.points} points')
            move_on = input('\n===== Press an WASD to Choose your Direction =====\n')

    if Playerinput != 'STAB':
        if Playerinput != 'LUNGE':
            if Playerinput != 'PUNCH':
                print ("Thats not even an option dude")
                points -= 5
                text_type(f"You have {points.points}.")
                move_on = input('\n===== Press an WASD to Choose your Direction =====\n')

### This can probably be used as a combat system in some fashion. ###