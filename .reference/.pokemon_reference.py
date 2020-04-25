# Simple battle simulator in the style of Pokemon.
# author: jane from allstate

import random

moves = {"tackle": range(18, 26),
         "thundershock": range(10, 36),
         "heal": range(10, 20)}


class Character:
    """ Define our general Character which we base our player and enemy off """
    def __init__(self, health):
        self.health = health

    def attack(self, other):
        raise NotImplementedError


class Player(Character):
    """ The player, they start with 100 health and have the choice of three moves """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        while True:
            choice = str.lower(input("\nWhat move would you like to make? (Tackle, Thundershock, or Heal)"))

            if choice == "heal":
                self.health += int(random.choice(moves[choice]))
                print("\nYour health is now {0.health}.".format(self))
                break
            if choice == "tackle" or choice == "thundershock":
                damage = int(random.choice(moves[choice]))
                other.health -= damage
                print("\nYou attack with {0}, dealing {1} damage.".format(choice, damage))
                break
            else:
                print("Not a valid move, try again!")


class Enemy(Character):
    """ The enemy, also starts with 100 health and chooses moves at random """
    def __init__(self, health=100):
        super().__init__(health)

    def attack(self, other):
        if self.health <= 35:
            # increasing probability of heal when under 35 health, bit janky
            moves_1 = ["tackle", "thundershock", "heal", "heal", "heal", "heal", "heal"]
            cpu_choice = random.choice(moves_1)
        else:
            cpu_choice = random.choice(list(moves))
        if cpu_choice == "tackle" or cpu_choice == "thundershock":
            damage = int(random.choice(moves[cpu_choice]))
            other.health -= damage
            print("\nThe CPU attacks with {0}, dealing {1} damage.".format(cpu_choice, damage))
        if cpu_choice == "heal":
            self.health += int(random.choice(moves[cpu_choice]))
            print("\nThe CPU uses heal and its health is now {0.health}.".format(self))


def battle(player, enemy):
    print("An enemy CPU enters...")
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health <= 0:
            break
        print("\nThe health of the CPU is now {0.health}.".format(enemy))
        enemy.attack(player)
        if player.health <= 0:
            break
        print("\nYour health is now {0.health}.".format(player))
    # outcome
    if player.health > 0:
        print("You defeated the CPU!")
    if enemy.health > 0:
        print("You were defeated by the CPU!")

if __name__ == '__main__':
    battle(Player(), Enemy())
	