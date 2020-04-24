from random import randint
import points


points.points_add()

def rock_paper_scissors():
    print ('''Hello,choose 1, 2, or 3
    1 beats 2, 2 beats 3, and 3 beats 1.
    The top number is your input, and the bottom number is the opponents input, 
    BEGIN''')
    Playerinput = input ()
    Gameinput = randint (1,3)
    print (Gameinput)
    if Gameinput == 1:
        if Playerinput == ('1'):
            print ('tie')
    if Gameinput == 1:
        if Playerinput == ('2'):
            print ('Your a Loser')
    if Gameinput == 1:
        if Playerinput == ('3'):
            points.points += 100
            print(f'Go Get em Girlfriend! You Win, and now have {points.points} points')

    if Gameinput == 2:
        if Playerinput == ('2'):
            print ('tie')
    if Gameinput == 2:
        if Playerinput == ('3'):
            print ('I knew you were a faliure when you first touched the keyboard')
    if Gameinput == 2:
        if Playerinput == ('1'):
            points.points += 100
            print (f'Winner Winner Chicken Dinner, you now have {points.points} points')

    if Gameinput == 3:
        if Playerinput == ('3'):
            print ('tie')
    if Gameinput == 3:
        if Playerinput == ('1'):
            print ('Your somehow managed to be bad at rock paper scissors, you lose')
    if Gameinput == 3:
        if Playerinput == ('2'):
            points.points += 100
            print (f'You Win! You now have {points.points} points')

    if Playerinput != '1':
        if Playerinput != '2':
            if Playerinput != '3':
                print ("Thats not even an option dude")

###This can probably be used as a combat system in some fashion.###