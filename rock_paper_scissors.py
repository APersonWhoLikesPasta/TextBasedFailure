from random import randint
import points, opponent
from technical import *


points.points_add()

def rock_paper_scissors():
    text_type("You have three attacks. You can LUNGE, PUNCH, or STAB.", 0.03)
    Playerinput = input('> ')
    Gameinput = randint (1, 3)
    print (Gameinput)
    
    # 1
    if Gameinput == 1:
        if Playerinput.upper() == ('STAB'):
            print(f'The {opponent.opponent} dodged your attack.')
    if Gameinput == 1:
        if Playerinput.upper() == ('LUNGE'):
            print ('You\'re a Loser.')
            
    if Gameinput == 1:
        if Playerinput.upper() == ('PUNCH'):
            points.points += 100
            print(f'Go Get em! You Win, and now have {points.points} points')
            
    # 2
    if Gameinput == 2:
        if Playerinput.upper() == ('LUNGE'):
            print(f'The {opponent.opponent} dodged your attack.')

    if Gameinput == 2:
        if Playerinput.upper() == ('PUNCH'):
            print('I knew you were a faliure when you first touched the keyboard')
            
    if Gameinput == 2:
        if Playerinput.upper() == ('STAB'):
            points.points += 100
            print(f'Winner Winner Chicken Dinner, you now have {points.points} points')
            
    # 3
    if Gameinput == 3:
        if Playerinput.upper() == ('PUNCH'):
            print(f'The {opponent.opponent} dodged your attack.')
            
    if Gameinput == 3:
        if Playerinput.upper() == ('STAB'):
            print(f"You died a horrible death, and made {opponent.opponent} very happy.")
            
    if Gameinput == 3:
        if Playerinput.upper() == ('LUNGE'):
            points.points += 100
            print(f'You Win! You now have {points.points} points')
            
    # Keyboard Mash
    if Playerinput.upper() != 'STAB':
        if Playerinput.upper() != 'LUNGE':
            if Playerinput.upper() != 'PUNCH':
                text_type("Thats not even an option dude.", 0.03)
                points.points -= 5
                print(f"You have {points.points}.")
                

### This can probably be used as a combat system in some fashion. ###\

