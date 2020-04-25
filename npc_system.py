import time
import random
import points
from opponent import *

points.points_add()

print("Battle Combat Init")

actions = {  # Don't forget the commas
    "PUNCH": 10,  # random.randrange(1, 10),
    "BANDAGE": 5  # random.randrange(2, 5)
}


class NPC:  # Defines base attributes for all entities
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(NPC):  # Start will 100 health
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        while True:
            player_choice = str.upper(input("\n How would you like to attack?"))
            print(actions)

            if player_choice == "BANDAGE":
                self.health += actions[player_choice]  # int(random.choice(actions[choice]))
                print(f"\nYour health is now {self.health}.")
            elif player_choice == "PUNCH":
                damage = actions[player_choice]  # int(random.choice(actions[choice]))
                other.health -= damage
                print(f"\nYou {player_choice} the {opponent}. You did {damage} damage.")
                break
            else:
                print("That's not even an option.")
                print("Try Again")
                time.sleep(0.5)


class Enemy(NPC):  # Chooses actions at random, start 100 health
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 35:  # Increase probability to heal when low health
            npc_actions = ["PUNCH", "BANDAGE", "BANDAGE", "BANDAGE"]  # Needs to be manually adjusted
            npc_action = random.randint(1, 4)  # Needs to be manually adjusted
            npc_choice = npc_actions[npc_action]
        else:
            npc_actions = list(actions.keys())
            npc_action = random.randint(0, 1)  # Needs to be manually adjusted
            npc_choice = npc_actions[npc_action]
        if npc_choice.upper() == "PUNCH":
            damage = actions[npc_choice]  # int(random.choice(actions[npc_choice]))
            other.health -= damage
            print(f"\nThe {opponent} attacks with {npc_choice}, and deals {damage} damage.")
        if npc_choice.upper() == "HEAL":
            self.health += actions[npc_choice]  # int(random.choice(actions[npc_choice]))
            print(f"\nThe {opponent} heals itself.")
            print(f"\nIt is now at {self.health} health.")


def battle(player, enemy):
    print(f"A smell {opponent} appears...")
    print(actions)
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            break
        print(f"\nThe health of the CPU is now {enemy.health}.")
        enemy.attack(player)
        if player.health <= 0:
            break
        print(f"\nYour health is now {player.health}.")
        # Outcome of Battle
    if player.health > 0:
        print(f"You defeated the {enemy}!")
    if enemy.health > 0:
        print("You lost bitch.")
    # Needs to be executed as `battle(Player(), Enemy())`
