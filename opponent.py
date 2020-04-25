from random import randint

global opponent
opponent = randint(1, 3)
if opponent == 1:
    opponent = "Troll"
elif opponent == 2:
    opponent = "Goblin"
else:
    opponent = "Creature"
