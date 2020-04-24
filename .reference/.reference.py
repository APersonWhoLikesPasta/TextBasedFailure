#A Hero's Journey
from random import randint
import sys
from time import sleep
def AddInventory (Item):
	Inventory.append(Item)
global gold
gold = 0

#To start adventure
TerminalGames = "{-}_{-}_{-}_/TERMINAL GAMES\_{-}_{-}_{-}"
for char in TerminalGames:
	sleep(0.001)
	sys.stdout.write(char)
	sys.stdout.flush()
print("")
GameName = "------------ A HEROES JOURNEY -----------"
for char in GameName:
	sleep(0.001)
	sys.stdout.write(char)
	sys.stdout.flush()
print("")
Credits = "===== BY CJ ZACH AND FRANKLIN ====="
for char in Credits:
	sleep(0.001)
	sys.stdout.write(char)
	sys.stdout.flush()
 

#Tutorial
print("""
Hello adventurer. In this adventure you will be making
many descions. The options will always be in CAPS. Your
input will always be in CAPS. If you input is not in 
caps you are not doing anything.""")

#To greet and discover the players name
player_name = input('Whats your name? >')
print(f"{player_name}.........interesting name but okay.")
Inventory = [] 
if player_name == 'epic gamer moment':
		print('You are a man of true culture.')
if player_name == 'Thanos':
	print('A snap is heard, and you are turned to dust.')
	exit(0)

	
#To find their class
_class = input('What class are you, a WIZARD, an ASSASSIN, or a KNIGHT? >')
#if input() == "":
#	print("You tried to skip this didnt you. Either you messed up, or your a cheeky little speedrunner. Nice try pal.")
#	exit(0)

#if _class != 'WIZARD':
#	if _class != "ASSASSIN":
#		if _class != "KNIGHT":
#			if player_name == 'LESBIANS':
#				if _class == 'FEMINIST':
#					print('Well, I guess that works.')
#					if player_name != 'LESBIANS':
#						if _class == 'FEMINIST':
#							print('Thats not a class!')
#							exit(0)
#Not working for some reason, zak fix p l s 
if _class == 'ASSASSIN' or 'KNIGHT' or 'WIZARD':
	print('Well I guess you do look like a ' + _class)

#To start adventure
LoadingBar = """[-] [-] [-] [-] [-] [-] [-] [-] [-]

"""
for char in LoadingBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

#Goblin Fight
print('A goblin stands in your way!')
attack_method = input('''
How will you attack it. 
Will you YELL at it or FLEE. >''')
if attack_method == 'YELL':#yell at goblin
		YELL = input('What are you going to yell? >')
		print(f"It seems {YELL} scared it away!")
		print('Looks like it dropped a sword and 10 gold!')
		AddInventory("Sword")
		gold = 10
		print (f'You have the following in your backpack:{Inventory}')
		print(f"You have {gold} gold")
elif attack_method == 'FLEE':#flee go lin
    print('''
You run for you life. As you rush down 
the hill you trip and fall. The flap of the 
goblins saggy skin and his moans make you 
shiver. You manage to escape. Barley.''')
elif attack_method != "YELL" or "FLEE":#do nothing

	print("You stand there, and do nothing. You DESERVE to DIE!!")
	print("YOU DIED")
	exit(0)
LoadingBar = """[-] [-] [-] [-] [-] [-] [-] [-] [-]

"""
for char in LoadingBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

#After Goblin
print(f"""
{player_name} sees two doors in the distance.
One door is blue and one is red.""")
print("There is a troll guarding both the doors! Press ENTER to continue.")
Outcome = input()
 
#Troll fight!
attack_method = input("""
Will you try to cast a SPELL, ATTACK it with a weapon 
or SNEAK past it? >""")
if attack_method == "SPELL":#Cast spell on troll
	if _class == 'WIZARD':#Wizard cast spell on troll
		print("""
You shout 'Avada Kadabra' and in a blast 
of green light the troll falls dead""")
		Outcome = 'SUCCESS'
		print(Outcome)
	if _class == "ASSASSIN":#Assassin cast spell on troll
		print("""
You try to cast a spell with some of 
the magic you heard about while on a mission in Elsewhere. 
Your spell is not powerful enough.""")
		Outcome = 'YOU DIED'
		print (Outcome)
		exit(0)
	if _class == 'KNIGHT':#Knight cast spell to fight troll
		print(f"""
You try to cast a spell. You are a knight. You are not 
a wizard {player_name}.""")
		Outcome = 'YOU DIED'
		print(Outcome)
		exit(0)
elif attack_method == 'ATTACK':
	if Inventory == ['Sword']:
		print('You attack it with a sword and you kill it!')
		Outcome = 'SUCCESS'
	if Inventory == []:
		print('You have nothing to attack with and the troll killed you!')
		Outcome = 'YOU DIED'
		exit(0)
elif attack_method == 'SNEAK':
	if _class == 'ASSASSIN':
		print('Your years of training have paid off as you sneak past the troll.')
		Outcome = 'SUCCESS'
	if _class == 'KNIGHT':
		print('The troll heard your clunky armor and killed you!')
		exit(0)
	if _class == 'WIZARD':
		print("""
You try to be sneaky, but you are a smelly geek. 
The dragons hears the swish of your rode, and 
gives you a wedgy.""")
		Outcome = 'YOU DIED'
		exit(0)
elif attack_method != "SPELL" or "SNEAK" or "ATTACK":
	print("You decided not to use a valid input!")
	print("YOU DIED")
	exit(0)
if Outcome == 'SUCCESS':#Outcome good
	print("You found a way to kill the troll, now which door will you choose?")
if Outcome == 'YOU DIED':#Outcome bad
	print("YOU DIED")
	exit(0)

	LoadingBar = """[-] [-] [-] [-] [-] [-] [-] [-] [-]

"""
for char in LoadingBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

#DoorsToChoose
door_choice = input('What door do you want, RED or BLUE? >')
if door_choice == 'BLUE':
	if _class == 'FEMINIST':#Feminist path
		print('You open the door and there stands...')
		print('BEN SHAPIRO DESTOYER OF LIBTARDS.')
		print('')
		print('Your going to have a very bad time.')
		print('As he says this his right eye starts glowing blue.')
		print('You can do two thing, become his enternal SLAVE or FIGHT him.')
		ben = input('>')
		if ben == 'SLAVE':
			print('You become his enternal slave.')
			exit(0)
		if ben == "FIGHT":
			print('You are stupid, he destroys you like every other libtard he has ever encountered. you are no different.')
			exit(0)

	#Blue Door
	open = input('This room has a treasure chest! Would you like to OPEN it, or LEAVE it be? >')
	if open == 'OPEN':
		Number = randint (1,2)
		if Number == 1:
			print('You open the chest and get 50 coins and a key')
			AddInventory("Key")
			gold = gold + 50
			print (f'You have the following in your backpack:{Inventory}')
			print(f"You have {gold} coins.")
			Outcome = "Back to the two doors!"
		if Number == 2:
			print('Turns out the chest is a mimic!')

		#Mimic Battle
		mimic_battle = input("Will you RUN away from it or ATTACK the mimic.>")
		if mimic_battle == 'RUN':
			print('You run away back to the two doors')
			Outcome = 'Back to the two doors.'
		if mimic_battle == 'ATTACK':
			weapon = input('There is a PIPE and a ROCK on the ground, which will you use to attack it? >')
		elif mimic_battle != 'ATTACK' or 'RUN':
			print("You tried to skip this didnt you. Either you messed up, or your a cheeky little speedrunner. Nice try pal.") #SKIP PATH
			exit(0)
			if weapon == 'ROCK':
				print('You through the rock at the mimic. The mimic laughs at you as it easily swipes the rock aside. It casually laughs at you, while slowly strangling you.' )
				print('YOU DIED!')
				exit(0)
			if weapon == 'PIPE':
				print('You whack it with a pipe and it dies.')
				print("")
				print('It also drops extra change, 50 more coins!')
				print('You return back to the two doors.')
				gold = gold + 50
				print(f"You have {gold} coins.")
				print (f'You have the following in your backpack:{Inventory}')
				print("")
	if open == 'LEAVE':
		print('Okay have it your way!')
	Outcome = "Back to the two doors!"
if Outcome == "Back to the two doors!":
	print('You go and open the red door and inside this door there is a great dragon!')
if door_choice == 'RED':
	print('You open the door to see a great red dragon.')

LoadingBar = """[-] [-] [-] [-] [-] [-] [-] [-] [-]

"""
for char in LoadingBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()

#DRAGON FIGHT!!!
print("You decide to advance through the red door.")
print("There is a dragon inside the chamber! The dragon looks very deadly, but nothing you can't handle!")
print("")
print("""
You have many choices, you can: Press A try to fight it, press B to talk your way through it, press C 
to bribe it with 60 gold,Press D to cast a confusion spell on the dragon, press E to sneak past it, 
press F to intimidate it, press G to try to tame it, press H to do nothing""")
print("")
dragon = input('What will you do?>')

#DragonFight
if dragon == 'A':
	print('You will try to fight the dragon!')
	dragon_kill = input('You can either MELEE the dragon, or SHOOT it with a ranged weapon. >')
	if dragon_kill == 'MELEE':#Melle Dragon
		print(player_name + ' Runs up to the dragon with a weapon.')
		weapon_choice = input('What weapon will you use, a SWORD, a HAMMER on the ground, or a PEBBLE? >')#Decide meelee weapon
		if weapon_choice == 'SWORD':#Sword Meelee
			if Inventory == ["Sword","Key"] or ["Sword"]:
				print('You stab the dragon with your sword!')
				Outcome = 'Dragon_Dead'
			if Inventory == [] or ["Key"]:
				print('You have no sword to attack it with!')
				print('YOU DIED')
		if weapon_choice == 'HAMMER':#Meelee hammer
			print('You pick up a nearby hammer!')
			hammer = input('Where will you hit the dragon, the HEAD or the TAIL? >')#Where to hammer dragon
			if hammer == 'TAIL':#Hammer tail
				print('The dragon howls in pain and flees!')
				Outcome = 'Dragon_Dead'
			if hammer == 'HEAD':#Hammer head
				print(player_name + ' hits the dragon hard across the head knocking a tooth out!')
				Outcome = 'Dragon_Dead'
				AddInventory("Dragon_Tooth")
				print (f'You have the following in your backpack:{Inventory}')
		if weapon_choice == 'PEBBLE':#Pebble
			print('Are you stupid?')
			print('Fine.')
			print(player_name + ' runs up to the dragon but then panics and picks up a pebble to slay the dragon.')
			print('The dragon feels pity and decided to become your friend.')
			print('Well, that worked.')
			AddInventory("dragon")
			print (f'You have the following in your backpack:{Inventory}')
			Outcome = 'Dragon_Friend'
	if dragon_kill == 'SHOOT':#Decide to shoot dragon with weapon
		print(player_name + " decides smartly to kill it from afar.")
		weapon_choice = input('will you choose a golden GUN nearby, your WAND or a ROCK? >')#Decide weapon
		if weapon_choice == 'GUN':#Gun
			print(player_name + ' picks up a gun nearby and shoots the dragon')
			aim = input('Where will you shoot it, the HEAD or the BODY>?')#Shoot head or body
			if aim == 'HEAD':#Shoot head
				print('You shoot the dragon with surprising accuracy.')
				Outcome = 'Dragon_Dead'
				print('Since the gun served you so well you decide to keep it.')
				AddInventory("Golden Gun")
				print (f'You have the following in your backpack:{Inventory}')
				print (f' the dragon also dropped 250 gold')
				gold = gold + 250
				print (f' you have {gold} gold')
			if aim == 'BODY':#Shoot body
				print('You should have gone for the head.')#not Cringy Thanos reference
				print('A snapping is heard in the distance as half the world is turned to dust, including you.')
				exit(0)
		if weapon_choice == 'WAND':#Use wand to fight dragon
			print("You decide to use a wand to kill the dragon.")
			if _class == 'WIZARD':#Wizard
				print('You cast a spell and the dragon dies!')
				Outcome = 'Dragon_Dead'
			if _class == 'KNIGHT':#Knight
				print('You cannot use magic spells!')
				print('YOU DIED')
				exit(0)
			if _class == 'ASSASSIN':#Assassin
				print('You cannot use magic spells!')
				print('You died!')
				exit(0)
		if weapon_choice == 'ROCK':
			print('You try to through the rock.')
			print('You missed')
			print('YOU DIED')
			exit(0)

#Talk to dragon
if dragon == 'B':
	print('You approach the dragon and say hello!')
	print(player_name + ': Hello Mr. dragon!')
	print('Dragon: Oh look my food is talking!')
	print(player_name + ": Oh you don't want to eat me!")
	print('Dragon: why not?')
	word = input('You can say the following: Press A to say In infected with mad human disease! or Press B to say I have a wife, kids and family! >')#Decide on how to convice dragon
	if word == 'A':#Convice dragon you have a disease
		print('Dragon: Well you know they say fire kills about 99% of bacteria.')
		word = input('You can say the following: Press A to say Well 1% can still kill you  or Press B to say Im immune to fire. >')#How convice dragon you are deadly
		if word == 'A':#You are the exception
			print('Dragon: Good thing I got my vaccine!')
			print('YOU DIED')
			exit(0)
		if word == 'B':#Convince the dragon you are immune to fire
			print('Dragon: No one is immune to fire.')
			print('YOU DIED')
			exit(0)
	if word == 'B':#Wife and kids argument
		print('Dragon: Do you think I care?')
		word = input('You can say the following: Press A to say well you should, I see your a mother too, and point to the dragon eggs, or press B to say nothing >')
		if word == 'A':#Snarkie response
			print("I see you are a mother too!")
			print('Dragon: *Thinks for a while*')
			print(f"{player_name} would you want to inflict that pain on someone?")
			print('Dragon: Fine go, you are free.')
			Outcome = 'Dragon_Dead'
		if word == 'B':#Be a pussy
			print('Dragon: Thats pitiful, I do not like to kill humans, but theres a first time for everything!')
			print('YOU DIED')
			exit(0)

#Bribe Dragon
if dragon == 'C':
	if gold == (60):
		print('The dragon accepts your payment and lets you move on.')
	if gold != (110):
		print('You attempt to scam the dragon, but the dragon realizes that you did not give him enough money, and he kills you.')
		print('YOU DIED')
		exit(0)

#Spell on Dragon
if dragon == 'D':
	if _class == 'WIZARD':#Class check
		print('You cast a very good confusion spell!')
		Outcome = 'Dragon_Dead'
	if _class != 'WIZARD':
		print('Why you decided to try to cast a spell when you are not a wizard is surprising. You should have learned by now.')
		print('The dragon kills you.')
		print('YOU DIED')
		exit(0)

#Sneak around the dragon
if dragon == 'E':
	if _class == 'ASSASSIN':#Class check
		print('You sneak past it with your sneaky sneak powers.')
	if _class != 'ASSASSIN':
		print('You are not sneaky!')
		print('The dragon kills you.')
		print('YOU DIED')

#Intimidate Dragon
if dragon == 'F':
    if _class == 'KNIGHT':#Class check
        print('The dragon is terrified by your shiny armor, and runs away!')
        Outcome = 'Dragon_Dead'
    if _class != 'KNIGHT':
        print('You are not intimidating, and you are burned to a crisp.')
        print('YOU DIED')
        exit(0)

#Try to tame dragon
if dragon == 'G':
	for X in range(10):
		if X == 1:
			print('You tamed the dragon!')
			Outcome = 'Dragon_Friend'
			AddInventory('Dragon')
			print(f'You have the following in your backpack {Inventory} ')
		if X != 1:
			print('You fail, and the dragon burns your skin until its some nice tasty Jack Links human jerky. Yum!.')
			print('YOU DIED')
			exit(0)
if dragon == 'H':
	print('You stand there, frozen at the face of danger and the dragon turns you to toast, burnt toast.')
	exit(0)

#Post Dragon
if Outcome == 'Dragon_Dead':
	print('You somehow managed to kill the dragon!')
	print('You also loot all of its gold!')
	gold = gold + 250
	print(f"You have {gold} coins.")
if Outcome == 'Dragon_Friend':
	print('You shove the dragon in your backpack.')
	LoadingBar = """[-] [-] [-] [-] [-] [-] [-] [-] [-]

"""
for char in LoadingBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()
print('You see a little shop in the distance, and you decide to head that way.')

#Shop
print('You run into a merchant in a wagon on the road.')
print("")
print (f'You have the following in your backpack:{Inventory}')
print(f"You have {gold} gold.")
print('''
The merchant is selling three items, an invisabilty potion, charisma potion, and a chest key.
Press "I" for a Invisibility Potion which costs 100.
Press "C" for a Charisma Potion which costs 100.
Press "K" for a Chest Key which costs 100.
Press "O" to buy quality air which costs 0 gold.''')
#Picking what to purchase
Desire = input()
if Desire == "I":
	if gold < 99:#To make sure you don't have negative gold
		print("FALIURE")
		print("YOU DIED")
		exit(0)
	if gold > 99:
		print("SUCCESS")
		AddInventory("Invisibility Potion")
		print(Inventory)
		gold = gold - 100
		print(f"You have {gold} gold.")
		MOO = input("Press 'Enter' to continue.")
if Desire == "C":#charisma potion
	if gold < 99:#To make sure you don't have negative gold
		print("You are bankrupt, and you starve to death.")
		print("YOU DIED")
		exit(0)
	if gold > 99:
		print("SUCCESS")
		AddInventory("Charisma Potion")
		print(Inventory)
		gold = gold - 100
		print(f"You have {gold} gold.")
		MOO = input("Press 'Enter' to continue.")
if Desire == "K":#Chest Key
	if gold < 99:#To make sure you don't have negative gold
		print("FALIURE")
		print("YOU DIED")
		exit(0)
	if gold > 99:
		print("SUCCESS")
		AddInventory("Chest Key")
		print(Inventory)
		gold = gold - 100
		print(f"You have {gold} gold.")
		MOO = input("Press 'Enter' to continue.")
if Desire == "O":#Preouim Oxygen
	print("You take a big gulp of air then bolt away before the merchant can stop you.")
	if gold < 0: #To make sure you don't have negative gold
		print("FALIURE")
		print("YOU DIED")
		exit(0)
	if gold > 0:
		print("SUCCESS")
		print(Inventory)
		print(f"You have {gold} gold.")
		MOO = input("Press 'Enter' to continue.")

LoadingBar = """[-] [-] [-] [-] [-] [-] [-] [-] [-] [-]  

"""
for char in LoadingBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()
print("You walk down the path with your newly acquired goods.")
print("You see three things in the distance.")
print("A 6ft tall cow grazes in the distance. You see the siloate of a village in the distance.")
print("A castle is also in the distance with a comically dark cloud overhanded the area.")#To split up the path a bit
Path = input('Do you go toward the VILLAGE, or the CASTLE. Or do you attempt want to kill the COW for food?>')
if Path == "COW":#You meet a cow with the power of MOTHER RUSSIA
	print("You walk toward the cow all casual like, but then the cow teleports away.")
	print("The cow appears behind you. The cows screams 'I will smite you with the power of MOTHER RUSSIA'.")
	print("You are turned to dust with a snap of the cows nonexistent figures.")
	print('YOU DIED')
	exit(0)
if Path == "VILLAGE":#Head to the village 
	print("You decide to take a look at the village. The castle looks a bit too ominous for you.")
	R = randint (1,3) #Chance to meet raiders
	if R == 1:#No raiders
			print("You safely make it to the village without any difficulty.")
			Outcome = "LUCKY"
			#FIRST RAIDER ENCOUNTER
	elif R == 2:#Fight raiders/talk way out of it
			print("As you walk down the path raiders jump out at you. They circle you from all angles. You appear to be trapped.")#Comes back to here after you kill bandits
			print('You can either FIGHT your way through it or you can TALK your way through it')
			bandit = input('>')
			if bandit == 'FIGHT':#If you decide to get rough and dirty with the bandits
				print('You will fight your way through it!')
				print('''
You could either try to SHOOT them with a gun, 
if you have any. You could try to kill them 
with a short DAGGER, maybe like a dragon 
fang, if you had a DRAGON you could scare 
them off, or PAY your way through it, however 
it will cost you 30 coins.''')
				print("")
				bandit_kill = input('>')
				if bandit_kill == 'SHOOT':#If you decide the pentrate them from afar(Shoot them)
					if "Golden Gun" in Inventory:
						print('You penetrate the raiders from afar.')
						Outcome = "WIN"
					else:
						print('Your hand twitches as you grab the gun at your waist belt, only to realize you dont have a gun.')
						print('That was a rookie gamerm mistake, and you got shot multiple times.')
						exit(0)
				if bandit_kill == 'DAGGER':#If you decide penetrate the bandits up close(Stab them)
					if "Dragon_Tooth" in Inventory:
						print('You are a sneaky snake and silently kill them all.')
						if _class == 'ASSASSIN':
							print(f"Since {player_name} is an assassin, {player_name} nabbed 70 coins off of the raiders.")
							gold = gold + 70
							print(gold)
							Outcome = "WIN"
						if _class != 'ASSASSIN':
							print('If only you were an assassin, you would have been able to be silent.')
							Outcome = "WIN" 
					else:
						print('You have no dragon tooth to attack them with!')
						exit(0)
				if bandit_kill == 'DRAGON':#Bring out your dragon
					if "Dragon" in Inventory:
						print('Your trusty friend flies out of your backpack and lets out a loud roar, the bandits run and hide.')
						Outcome = "WIN"
					else:
						print('You stand there calling your dragon out of your backpack, the bandits stare at you wondering what the heck you were doing and feel pity for you,')
						print('The bandits walk away slowly, as they believe you are insane.')
						print('You made it!')
						print('A thunder is heard as quite suddenly exactly 18.341290 bolts of lightning kill you.')
						exit(0)
				if bandit_kill == 'PAY':#If you want to pay the bandits
					print('You attempt to pay the bandits money.')
					if gold >= 30:
						print('You pay the bandits and they leave.')
						gold = gold - 30
						Outcome = "WIN"
					if gold <= 30:
						'The bandits see that they short changed you and kill you.'
						exit(0)
			if bandit == 'TALK':#Get your lips loose (talk to bandits)
				print('You will try to talk your way through it.') #ADD CHARISMA POTION OPTION.
				print('What do you want to do LIE, CONVINCE them, or use your CHARISMA potion.')
				talk = input('>')
				if talk == 'CHARISMA':#To use potion
					if 'Charisma Potion' in Inventory:
						print("""
You drink your charisma potion. 
Suddenly the bandits look at you with 
love in their eyes. They say in unison 
'Can we kiss yoooou?' You run for your life. The 
bandits follow you, but because they 
are high on love they can only manage 
a stumbling run. One faceplants into 
the ground.""")
						Outcome = 'WIN'
					else:
						print("You don't have a charisma potion dummy.")
						print("The bandits are hungry and decide to eat you.")
						print("YOU DIED")
						exit(0)
				if talk == 'LIE':#Decide to be sneaky
					print('You can either say that I will use the power of the GODS on you')
					print('or you can say')
					print('I am a billionaire and if you let me go, I will give you MILLIONS!')
					_talk = input()
					if _talk == 'GODS':#To pretend to be god				
						if _class == "WIZARD":#Class check
							print('You use your wizarding skills and they are impressed')
							Outcome = "WIN"
						if _class != "WIZARD":
							print('The bandits think for a bit, you are surprised you made it this far.')
						print('Bandits: prove it')
						print(f'{player_name} :what?')
						print('Bandits: prove you have the power of the gods.')
						print(f'{player_name}ummmmmm')
						print("The bandits realize you have no power, and they kill you.")
						exit(0)
					
					if talk == "MILLIONS":#Pretend to be rich
						print('The bandits look skeptical')
						print('The bandits say that you need to prove it.')
						print('You can either make a RUN for it, or SHOW them some of your riches, beware, they may take it')
						bandit_bribe = input()
						if bandit_bribe == 'RUN':#You try to run form bandits
							print('You make a run for it it, and the bandits chase you!')
							print('You end up loosing them only because they wouldnt follow you up to the castle.')
							Outcome = 'to the castle'
						if bandit_bribe == 'SHOW':#You show your gold
							if gold >= 200:
								print('They see the whopping pile of gold, and are tempted')
								print('You see that you could possibly have them work for you with that amount of money,would you like to hire them. YES or NO')
								bandit_hire = input()
								if bandit_hire == 'YES': #you hire bandits
									print('You pay the bandits and they join your team, you could always use some help')
									AddInventory('Bandit_Team')
									Outcome = "WIN"
								if bandit_hire == 'NO':#You don't hire bandits
									print('The bandits leave you knowing that you are rich and will pay them in the future')
									Outcome = 'WIN'
							if gold <= 200:#You don't have enough gold
								print('The bandits see that the only thing in your wallet is a 56 cent gift card for Applebees. They kill you.')
								exit(0)
								
#SECOND BANDIT ONE
			if R == 3:
				print("As you walk down the path, a group of raiders jump out at you. They circle you from all angles. You appear to be trapped.")#Comes back to here after you kill bandits
				print('You can either FIGHT your way through it or you can TALK your way through it')
			bandit = input('>')
			if bandit == 'FIGHT':#If you decide to get rough and dirty with the bandits
				print('You will fight your way through it!')
				print('''
You could either try to SHOOT them with a gun, 
if you have any. You could try to kill them 
with a short DAGGER, maybe like a dragon 
fang, if you had a DRAGON you could scare 
them off, or PAY your way through it, however 
it will cost you 30 coins.''')
				print("")
				bandit_kill = input('>')
				if bandit_kill == 'SHOOT':#If you decide the pentrate them from afar(Shoot them)
					if "Golden Gun" in Inventory:
						print('You shoot the raiders')
						Outcome = "WIN"
					else:
						print('Your hand twitches as you grab the gun at your waist belt, only to relies you dont have a gun.')
						exit(0)
				if bandit_kill == 'DAGGER':#If you decide penetrate the bandits up close(Stab them)
					if "Dragon_Tooth" in Inventory:
						print('You are a sneaky snake and silently kill them all.')
						if _class == 'ASSASSIN':
							print(f"Since {player_name} is an assassin, {player_name} got 70 coins off of the raiders.")
							gold = gold + 70
							print(gold)
							Outcome = "WIN"
						if _class != 'ASSASSIN':
							print('If only you were an assassin, you would have been able to be silent.')
							Outcome = "WIN" 
					else:
						print('You have no dragon tooth to attack them with!')
						exit(0)
				if bandit_kill == 'DRAGON':#Bring out your dragon
					if "Dragon" in Inventory:
						print('Your trusty friend flies out of your backpack and lets out a loud roar, the bandits run and hide.')
						Outcome = "WIN"
					else:
						print('You stand there calling your dragon out of your backpack, the bandits stare at you wondering what the heck you were doing and feel pity for you,')
						print('The bandits walk away slowly, as they believe you are insane.')
						print('You made it!')
						print('A thunder is heard as quite suddenly exactly 18.341290 bolts of lightning kill you.')
						exit(0)
				if bandit_kill == 'PAY':#If you want to pay the bandits
					print('You attempt to pay the bandits money.')
					if gold >= 30:
						print('You pay the bandits and they leave.')
						gold = gold - 30
						Outcome = "WIN"
					if gold <= 30:
						'The bandits see that they short changed you and kill you.'
						exit(0)
			if bandit == 'TALK':#Get your lips loose (talk to bandits)
				print('You will try to talk your way through it.') #ADD CHARISMA POTION OPTION.
				print('What do you want to do LIE, CONVINCE them, or use your CHARISMA potion.')
				talk = input('>')
				if talk == 'CHARISMA':#To use potion
					if 'Charisma Potion' in Inventory:
						print("""
You drink your charisma potion. 
Suddenly the bandits look at you with 
love in their eyes. They say in unison 
'Can we kiss yoooou?' You run for your life. The 
bandits follow you, but because they 
are high on love they can only manage 
a stumbling run. One faceplants into 
the ground.""")
						Outcome = "WIN"
					else:
						print("You don't have a charisma potion dummy.")
						print("The bandits are hungry and decide to eat you.")
						print("YOU DIED")
						exit(0)
				if talk == 'LIE':#Decide to be sneaky
					print('You can either say that I will use the power of the GODS on you')
					print('or you can say')
					print('I am a billionaire and if you let me go, I will give you MILLIONS!')
					_talk = input()
					if _talk == 'GODS':#To pretend to be god
						print('The bandits think for a bit, you are surprised you made it this far.')
						print('Bandits: prove it')
						print(f'{player_name} :what?')
						print('Bandits: prove you have the power of the gods.')
						print(f'{player_name}: ummmmmm')
						
						if _class == "WIZARD":
							print('They are very impressed with your awesome magic.')
							Outcome = 'WIN'
						if _class != "WIZARD":
							print('You stand there, doing nothing, and the bandits kill you for lying.')
							exit(0)
					if talk == "MILLIONS":#Pretend to be rich
						print('The bandits look skeptical')
						print('The bandits say that you need to prove it.')
						print('You can either make a RUN for it, or SHOW them some of your riches, beware, they may take it')
						bandit_bribe = input()
						if bandit_bribe == 'RUN':#You try to run form bandits
							print('You make a run for it it, and the bandits chase you!')
							print('You end up loosing them only because they wouldnt follow you up to the castle.')
							Outcome = 'to the castle'
						if bandit_bribe == 'SHOW':#You show your gold
							if gold >= 200:
								print('They see the whopping pile of gold, and are tempted')
								print('You see that you could possibly have them work for you with that amount of money,would you like to hire them. YES or NO')
								bandit_hire = input()
								if bandit_hire == 'YES': #you hire bandits
									print('You pay the bandits and they join your team, you could always use some help')
									AddInventory('Bandit_Team')
									Outcome = "WIN"
								if bandit_hire == 'NO':#You don't hire bandits
									print('The bandits leave you knowing that you are rich and will pay them in the future')
									Outcome = 'WIN'
							if gold <= 200:#You don't have enough gold
								print('The bandits see that the only thing in your wallet is a 56 cent gift card for Applebees. They kill you.')
								exit(0)
					
			LoadingBar = """[-] [-] [-] [-] [-] [-] [-] [-] [-] [-]  

"""#AddInventory needs to have the 'A' in Add captilised
for char in LoadingBar:
	sleep(0.05)
	sys.stdout.write(char)
	sys.stdout.flush()
	#Thought it was weird that it was sticking out only after gods so I put loading bar here.

#Judge if you won with bandits or not
if Outcome == "WIN":
	print("You make it to the village after the firghtful encoutner with the bandits.")
if Outcome == "Lucky":
	print("You make it to the village without much diffculty.")

#VILLAGE!
def Village (WayYouArrived):
	print('The village seems peaceful, there is a nice SHOP, a WELL, a CHURCH , a MINE and a town SQUARE.')
	print('Were do you want to go first')
	village_path = input('>')

	#Village Shop
	if village_path == 'SHOP':
		print('You have {gold} gold')
		print('You walk up to the nice merchant, he smiles at you and offers you three things, A CHARISMA potion (100) , a LOOTING potion (100) and a nuclear WARHEAD (may be helpful in final boss battle) (500) or do you KILL him, for 0 coins')
		print('so what will it be?')
		desire = input()
		if desire == 'CHARISMA':
			if gold > 99: 
				if gold >= 100:
					print('You buy the charisma potion.')
					AddInventory('CHARISMA')
					gold = gold - 100
					print (f' You have {Inventory} in your backpack')
					print (f' You have {gold}')
			if gold < 99:
				print('You are broke!')  #exuse what the fuc
				print('The merchant whips out a golden scar and does take the L while you dance due to a boogie bomb. Mother russia  proud of its minion as it eliminates democratic system. The soviet russian anthem plays as the bullets rip through your cheast, you fall slowly to the ground, people rush out of the town square, tea bagging your dead body. Suddenly a large BOOM is heard in the distance as a nuclear warhead is detonated, you become instantly cremated.')
				print('needless to say, YoU dIeD')
				exit(0)
		if desire == 'LOOTING':
			if gold > 99:
				if gold >= 100:
					print('You purchase a looting potion.')
					AddInventory('LOOTING')
					gold = gold - 100
					print (f'You have {Inventory} in your backpack.')
					print (f'You have {gold} gold.')
				if gold <= 100:
					print('You dont have enough money, the merchant killed you!')
					exit(0)
			if gold < 99:
				print('You are broke')	
				print('The merchant does a double roundhouse kick and knocks your head off')
				exit(0) #dragon
		if desire == 'WARHEAD':
			print('The merchant casually whips out a 50 foot nuclear warhead.')
			if gold > 499:
				if gold >= 500:
					print('You spent all of your money on a bomb, congratulations')
					AddInventory("NUKE")
					gold = gold - 500
					print('You have {gold} gold!')
				if gold <= 500:
					print('You can buy that!')
					print('The merchant detonates the nuke by accident and you die')
					exit(0)
			if gold < 499:
				print('You are broke, you cannot buy a bomb!')
				print('The merchant sees that you are broke and homeless so he kills you.')#???
				exit(0)
		if desire == "KILL":
			print('You pull out a ak-47 and open fire.')
			print('You also acciedntly hit the nuclear warhead.')
			print('''KABOOOOOOOM''')
			exit(0)
		else:
			print('Thats wasnt an option!')
			print('The mercahnt sees that you didnt want to buy something that was in his shop and whips out a bazooka and turns you into smitherines.')
			print('That was unexpected.')
			exit(0)
	if village_path == 'WELL':
		print('You walk to the old well and put the bucket to the bottem, hopefully you could get something goood!')
		for X in range(1,5):
			if X == 1:
				print('You fish up.......')
				print('WATER')
				print('You were sad, as a nuclear warhead did not come out of the well.')
		if X == 2:
			print('You fish up...... ')
			print('A KEY!')
			AddInventory('Key')
			print('You have {Inventory} in your backpack!')
		if X == 3:
			print('You fish up.....')
			print('A bunch of gold!')
			print('50 gold, thats not bad')
			gold = gold + 50
		if X == 4:
			print('You fish up.....')
			print('a chest!')
			print('If only you had a key to open it.')
			if 'Key' in Inventory:
				print('Wait, you do!')
				print('Would you like to OPEN the chest, or SAVE your key for possibly later better chests')
				Key = input('>')
				if Key == "OPEN":
					if 'Dragon_Tooth' in Inventory:
						if 'Golden Gun' in Inventory:
							print('how did you get here what.!')
						else:
							print('You find a really cool golden gun, an awesome find!')
							AddInventory('Golden Gun')
					else:
						print('In the chest there is a cool dragon fang dagger')
						AddInventory('Dragon_Tooth')
				if Key == 'SAVE':
					print('Good idea, there might be more along the road.')
		if X == 5:
			print('As you pull up the bucket it seems abnormally heavy, you use all of your muscle mass and you find.....')
			print('A Large ROCK!')
			print('Very anticlimatcic')
			print('For some reason you keep the enormous thing. He is now your pet boulder. You call him, J.D ROCKerfeller.')
			AddInventory('Pet Boulder')

#church #meowing nuns
	if village_path == 'CHURCH':
		print('You approach the church, a deep humming noise is heard.')
		print('after further investigation you now know that it was not humming, it was meowing')
		print('the meowing grows louder')
		print('Do you want to go into the CHURCH or just MOVE on.')
		church = input()
	if church == 'CHURCH':
		print('You enter the church and see that the meowing is coming from the nuns')
		print("Why, you may be asking. Well we don't know, us devs are weird and we though that would be funny.")
		print(f'Well our hero {player_name} is faces with a tough predicament {player_name} could either nicely ask them to ASK, so you could investsigate the church or JOIN them')
		nuns = input('>')
		if nuns == 'JOIN':
			print('You start meowing and feel oddly blissful')
			print('You meow and meow and you slowly start to lose track of time and your surrounding')
			print('You slowly become nothing but a meowing puppet, your life becomes nothing but meowing. you become the embodiment of a cat.')
			print('What else did you expect to happen? By the way, you meowed yourself to death.')
			exit(0)
		if nuns == 'ASK':
			print("You ask the nuns to leave but they don't seem to hear you.")
			print("You ask louder and louder, but they don't hear you, they just keep meowing.")
			print('You can either do this by FORCE or BARK like a dog to counter their persian ways.')
			nun_kill = input('>')
			if nun_kill == "FORCE":
				print('you shove your way through the nuns, knocking them over, the dont seem to care, they just keep meowing.')
				print('you somehow resist the temptation to join them and make it through!')
				print('there is a door in the back, maybe this could be the answer to the meowing?')
				print('do you want to open it? YES or NO')
				door = input()
				if door == "YES":
					print('You open the door to see a bunch of priests and parishiners huddled over a fire, the look harrarg and ware worn, most of them look like they have not eaten in days ')
					print(f'{player_name}: WAHT HAPPENED!')
					print('The preists look terrified, they explain how once a nun started meowing they all did, and soon everyone was meowing, you see that this small camp has been hiding here for days maybe weeks or months.')
					print('You decide to free them')
					print('How will you do it, will you blow a HOLE in the wall, or will you tell them to BARK with you in unison')


# Walk to castle
walk = 'at the castle'
if Path == 'CASTLE':
	print('You walk up the dark path, you shudder at the sight of it, are you sure you want to continue? YES or NO')#Check nerve
	_continue = input()
	if _continue == 'YES':
		print("A deep howl is heard in the distance, it wasn't a wolf")
		print('Do you want to continue? YES or NO?')
		__continue = input()
		if __continue == 'YES':
			print('Really')
			print("Im not going to keep the suspense, this is literally a suicide missoin, I'm doing this for your own health")
			print('But I cant force you to do anything, (sigh) do you want to continue. YES or NO?')
		___continue = input()
		if ___continue == 'YES':
			print('Why would you do that, are you stupid!')
			print('Despite my warnings you make it to the dark castle, your instincs seem to be screaming at you.')
			walk = 'at the castle'
		if ___continue == "NO":
			print('Thank You')
			walk = 'Turn_back'
		if __continue == 'NO':
			print('Good decision')
			walk = 'Turn_back'
	if _continue == 'NO':
		print('Good decision')
		walk = 'Turn_back'

if Outcome == 'To the castle':
	print('The castle looks evil, your bones and blood seem to chill at the sight of it')
	walk = 'castle'

	if walk == 'at the castle':
		print('You enter the castle, you know you made a mistake')
	if walk == 'Turn_back':
		print('You made the right choice')
		print('As you walk back a group of bandits jump you and kill you. I mean, what are the odds of that happening')
	exit(0)

#Castle
walk = input()
print('The castle looks like it has not been used in years, but the feeling in your body says otherwise')
print('A swishing noise is heard as a dark hooded figure glides towards you, this is no ordinary castle')
if walk == 'at the castle':
	print('I told you so')
print('The hooded figure seems evil, you must defeat it.')
print("Please Play again soon, more content will be added in the future")
