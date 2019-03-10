'''
Game Name: Blood, Sweat & Loot (or Dawn of War)
Creator: Rafael (nelson450)

Ideas:
-Factions: Holy ... Empire, Albion Confederacy, Geroia Republic, etc.
-Tkinter Scale for betting on races and dices in tavern
-Lords and merchants personalities(grumpy etc.)
-RadioButtons for selecting backgorund history(son of: noble, peasant, clergy etc)
-Castle and Village upgrades
-Special places like monasteries, bandit camps, old ruins and caves
-Intelligence, Agility,Charisma,Strongness
-Works for villagers, like Blacksmith, Woodcutter or Farmer
-Taxes, Trade Taxes, Honour(slavery, culture), Renown, Laws, Politicpower etc.
-Hammurabi-like management
-One market per faction or one in every castle?
-Soldiers can run away, flee battle, lose morale etc.
-Industries law: silk, gold, church...
-Use Clint, Time, msvcrt and other cool modules...
-Add option "Good bye cruel world..." (WTF?)
-Add family management(give your daughter etc.)
-and more...
---> only kingdom management or also adventuring?
'''

from random import randint, choice
from math import ceil, floor

class Character:
	def __init__(self):
		self.name = ''
		self.health = 100
		#self.strength=0
		self.speech = 0 #and also it?
		#self.socialclass='' #remove it?
		self.coins = 0
		#self.renown=0 #what it does?
		self.honour = 0
		#self.fear=0 #fear == powerpoints?
		self.inventory = []
		#self.stamina=0   no stamina!
	def status(self):
		return "%s's current health is %d." % (self.name, self.health)
	def __repr__(self):
		return 'Do something with the object!'

'''class Player(Character):
	def __init__(self):
		Character.__init__(self) #the same of super().__init__
		#self.stamina=5
		#self.map_position=map_position #???
	def sleep(self):
		if self.stamina<=5:
			return '%s is already fresh!' % self.name
		else:
			self.stamina+=1
	def change_socialclass(self, newsocialclass): #remove?
		self.socialclass=newsocialclass
	def status(self):
		return "%s's current health is %d." % (self.name, self.health)'''

class Troop(Character): #put it under Army?
	def __init__(self, name, payment): #put types: infantry, cavalry, siege?
		Character.__init__(self)
		self.name = name
		self.attack = {'missile': 0, 'melee': 0, 'thrusting': 0}
		self.defense = {'missile': 0, 'melee': 0, 'thrusting': 0} #defense against...
		#self.chief=chief
		self.wounded = False #put xp points for training? NO
		self.payment = payment
	def pay(self): #move method?
		if self.chief.coins < self.payment: #needs improvement for morale?
			if randint(0,1):
				return self.flee() #improve it!
			else:
				return "Soldiers are grumbling because you didn't pay them!"
		self.chief.coins -= self.payment
	def upgrade(self): #not necessary?
		pass
	'''def flee(self): #move it all to Army?
		self.chief = None
		self.payment = None
		return 'One %s fled to the woods.' % self.name'''

class Army:
	def __init__(self, chief, faction): #sell troops etc
		self.chief = chief
		self.faction = faction
		self.morale = 100
		self.troops = [] #put a dict here?
	def flee(self):
		if self.morale < 70:
			self.troops.remove()
	def attack(self):
		pass
	def feed(self):
		pass

class Kingdom: #add specialists: spy, diplomat etc
	def __init__(self, name, ruler): #shouldn't pass parameters?
		self.ruler = ruler
		self.name = name
		self.description = description
		#self.vassals = vassals   NO VASSALS???
		self.powerpoints = 100
		#self.treasury = 5000
		#self.ruler.socialclass = 'noble' #when you rule you are a noble
		self.trooptree = {}
	def __str__(self): #add spying?
		return self.description + "No more info about them available..."

	def diplomacy(self, faction): #put all diplomacy out of class?
		pass

class Castle: #shouldn't inherit? yeah
	def __init__(self, ctlname, faction, lord):
		#Kingdom.__init__(self, ruler, vassals)
		self.castle_name = ctlname
		self.lord = lord
		self.faction = faction
		#self.capital = False #main city?
		self.level = 1
		self.defensebonus = 1.05
		self.population = randint(90, 110) #change to workers?
		self.warehouse = {'food': 250, 'stone': 150, 'wood': 100, 'iron': 100}
		self.garrison = Army(self.lord, faction)
	def upgrade(self):
		if self.level >= 5:
			return "Can't upgrade beyond 5th level!"
		if self.warehouse['food'] < 50 * self.level:
			return "Not enough resources!"
		self.faction.powerpoints += 10 * self.level
		self.lord.coins -= 500 * self.level
		self.level += 1
		self.population += 5 * self.level #put new workers or deaths by accident?
		self.defensebonus += 0.1
		self.warehouse['food'] -= 50 * self.level
		self.warehouse['stone'] -= 150 * self.level
		self.warehouse['wood'] -= 100 * self.level
		self.warehouse['iron'] -= 50 * self.level
	def recruit(self, troopnumber):
		if troopnumber > self.population // 3:
			return "Can't recruit so much troops!"
		self.population -= troopnumber
		return "You recruited %d militiamen." % troopnumber
	def traintroops(self, number):
		#self.garrison
		pass
	def jobs(self, percentage_list):
		jobs = {'farmers':0.5, 'stonecutters': 0.2, 'lumbermen': 0.15, 'blacksmiths': 0.15} #default
		if percentage_list or type(percentage_list) != list: #if True ==> default
			return "Job list changed to default."
		for i, j in zip(list(jobs), percentage_list):
		  jobs[i] = j
	  return jobs
	def collect_tax(self, taxlvl):
		self.lord.coins += self.population * taxlvl
		self.population -= ceil(taxlvl) #people leave when taxes are abusive

	@staticmethod
	def weather(): #move method to outside???
		weather_list = {'heavy snow': 0.5, 'stormy day': 0.75, 'normal day': 1, 'another normal day': 1, 'sunny day': 1.25, 'blessed day': 1.5}
		return choice(list(weather_list.items()))
	'''def check_warehouse(self): #bad method???
		loadout=500*self.level
		if sum(self.warehouse.values) > loadout: #REMOVE THIS CRAP!
			return True
		return False'''
	def feed(self, sacks): #troops also deserve food!
		mouths = self.population + len(self.garrison)
		starved = self.population - sacks
		print('You need to feed %d hungry jaws!' % mouths) #move this to main.py?
		if self.warehouse['food'] < 2:
			dead=randint(starved // 2, starved-2)
			self.lord.honour -= 5
			self.population -= dead
			return 'You have nothing to feed your people!!!\n%d peasants died or fled'%dead
		elif sacks > self.warehouse['food']:
			return print("You don't have so much grain!\nPlease type again...")
			#self.feed(sacks) #recursion error!
		elif starved <= 0:
			newpeople = randint(2, abs(starved)+1)
			self.lord.honour += 1
			self.lord.renown += 5
			self.warehouse['food'] -= sacks
			self.population += newpeople
			return 'After hearing about the plenty of grain in your lands, %d wandering peasants decide to live in %s castle!' % (newpeople, self.ctlname)
		elif starved > 10:
			self.lord.honour -= 1
		self.warehouse['food'] -= sacks
		self.population -= starved
		return 'You have fed %d people, but %d starved.' % (sacks, starved)
	def harvest(self):
		self.warehouse['food'] += self.population * 2 * self.weather()[1]
		return self.weather()[0]
	def choptrees(self): #put it on harvest?
		self.warehouse['wood'] += self.population
	def hunt(self): #hunting provides additional food
		gamelist = {'hare': 10, 'fox': 20, 'deer': 45, 'wolf': 60, 'bear': 100, 'bison': 130} #animal: food units

	def raid(self, raiderpower): #raiders can't occupy castle only damage it
		pass
	def conquer(self, invader):
		self.lord=invader
		pass

class Item:
	"""Defines an item that can be bought on market"""
	def __init__(self, name, amt, value):
		self.name = name
		self.description = ''
		self.amt = amt
		self.value = value#+(value//self.amt) #supply/demand law
	def regulate_price(self):
		if self.amt == 5:
			return 'Normal price.'
		if self.amt > 5:
			self.value -= self.value//self.amt
			return 'Prices dropped.'
		self.value += self.value//self.amt
		return 'Prices got raised.'
	def __str__(self):
		return self.description

class Market: #change it to tavern?
	"""This is the kingdom's Great Market, where you can buy and sell items, recruit mercenaries or just drink some wine!"""
	def __init__(self, lord):
		self.lord = lord
		self.level = 1
		self.stock = {} #set!
	def upgrade(self):
		print("Upgrading allows you to buy more items per level!")
		if self.lord.coins < 500*self.level:
			return 'Not enough money!'
		if self.level >= 3:
			return "Can't upgrade beyond 3rd level!"
		self.level += 1
		self.lord.coins -= 500*self.level
	def buy(self, item): #add option to buy all stock?
		if item not in self.stock or item.amt < 1:
			return 'Item not available!'
		if self.lord.coins < item.value:
			return "Not enough money!"
		item.amt -= 1
		item.regulate_price()
		self.lord.coins -= item.value
		self.lord.inventory.append(item)
		return '%s was bought.' % item.name
	def sell(self): #sell also soldiers?
		pass
	def tavern(self): #remove tavern from market??
		print("Welcome to the tavern! Here you can play dice, buy ale and listen to bards.")
		pass