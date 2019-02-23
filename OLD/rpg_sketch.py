'''
THIS IS A DOCSTRING!!!
Game Name: Blood, Sweat & Loot
Creator: Rafael

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
-and more...
---> only kingdom management or also adventuring?
'''

from random import randint
from math import ceil, floor

class Character:
    def __init__(self):
        self.name='randomplayer'
        self.health=100
        self.strength=0
        self.speech=0
        self.socialclass=''
        self.coins=0
        self.renown=0
        self.honour=0
        self.fear=0
        self.inventory=[]
        #self.stamina=0   no stamina!
    def __repr__(self):
        return 'Do something with the object!'

class Player(Character):
    def __init__(self): #map_position
        Character.__init__(self) #the same of super().__init__
        #self.stamina=5
        #self.map_position=map_position #???
    '''def sleep(self):
        if self.stamina<=5:
            return '%s is already fresh!' % self.name
        else:
            self.stamina+=1'''
    def change_socialclass(self, newsocialclass): #remove?
        self.socialclass=newsocialclass
    def status(self):
        return "%s's current health is %d." % (self.name, self.health)
    def recruit(self): #move to class Party???
        pass

class Troop(Character):
    def __init__(self, name, chief, payment):
        Character.__init__(self)
        self.name=name
        self.attack={'missile':0, 'melee':0, 'thrusting':0}
        self.defense={'missile':0, 'melee':0, 'thrusting':0} #against...
        self.chief=chief
        self.wounded=False
        self.payment=payment
    def pay(self):
        self.chief.coins -= self.payment
    def upgrade(self): #not necessary?
        pass

class Kingdom:
    def __init__(self, name, ruler, vassals): #shouldn't pass parameters?
        self.ruler=ruler
        self.name=name
        self.vassals=vassals
        self.powerpoints=100
        self.treasury=5000
        self.ruler.socialclass='noble' #when you rule you are a noble
    def diplomacy(faction):
        pass

class Castle(Kingdom):
    def __init__(self, ctlname, lord): #errors
        Kingdom.__init__(self)
        self.ctlname=ctlname
        self.lord=lord
        self.level=1
        self.defensebonus=1.05
        self.population=randint(90, 110) #change to workers?
        self.warehouse={'food':200, 'stone':100, 'wood':100, 'iron':100}
        self.garrison=250
    def upgrade(self):
        if self.level >= 4:
            return "Can't upgrade beyond 3rd level!"
        if self.warehouse['food'] < 50*self.level:
            return "Not enough resources!"
        #self.powerpoints+=10*self.level
        self.lord.coins-=500*self.level
        self.level+=1
        self.population+=5*self.level #new workers in castle
        self.defensebonus+=0.1
        self.warehouse['food'] -= 50*self.level
        self.warehouse['stone']-=150*self.level
        self.warehouse['wood']-=100*self.level
        self.warehouse['iron']-=50*self.level
    def recruit(self, number):
        if number>self.population//3:
            return "Can't recruit so much troops!"
        self.population-=troopnumber
        return "You recruited %d militiamen." % troopnumber
    def traintroops(self, number):
        pass
    def village_jobs(self):
        jobs={'farmers':0.25, 'stonecutters':0.25, 'lumbermen':0.25, 'blacksmith':0.25}
    def collect_tax(self, taxlvl):
        self.lord.coins+=self.population*taxlvl
        self.population-=ceil(taxlvl) #people leave when taxes are abusive
    def weather(self): #move method to outside???
        weather_list={'heavy snow':0.5, 'stormy day':0.75, 'normal day':1, 'another normal day':1, 'sunny day':1.25, 'blessed day':1.5}
        return choice(list(weather_list.items()))
    def check_warehouse(self): #bad method???
        loadout=500*self.level
        if sum(self.warehouse.values)>loadout:
            return True
        return False
    def feed(self, sacks): #troops also deserve food!
        print('You need to feed %d hungry serfs!' % self.population) #move this to main.py?
        if self.warehouse['food']<2:
            return 'You have nothing to feed your people!!!\n%d peasants died or fled'%randint(self.population//2,self.population-2)
        elif sacks > self.warehouse['food']:
            print("You don't have enough grain!\nPlease type again...")
            self.feed(sacks)
        elif sacks >= self.population:
            #honour, renown+=...
            self.lord.honour+=1
            self.lord.renown+=5
            self.warehouse['food']-=sacks
            return 'After hearing about the plenty of grain in your lands, %d wandering peasants decide to live in %s castle!' % (randint(1, sacks-self.population), ctlname)
        self.warehouse['food']-=sacks
        return 'You have fed %d people, but %d starved' % (sacks, self.population-sacks)
    def harvest(self):
        self.warehouse['food'] += self.population*2*self.weather()[1]
        return self.weather()[0]
    def choptrees(self):
        self.warehouse['wood'] += self.population
    def raid(self, raiderpower): #raiders can't occupy castle only damage it
        pass
