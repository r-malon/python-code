class Bank:
	def __init__(self, name, money_reserve):
		self.name = name
		self.__users = dict()
		self.__money = money_reserve
	def movement(self, amount):
		self.__money += amount

class User:
	def __init__(self, name, starting_money, agency):
		self.name = name
		self.__money = starting_money
		self.agency = agency
		self.__psw = password
		self.operations = {'sacks': 0, 'lends': 0}
	def sack(self, amount):
		self.agency.movement(amount)
		self.operations['sacks'] += 1
	def login(self):
		pass
	def view_balance(self):
		return f'{self.name} currently has ${self.__money} and made\
		 {self.operations["sacks"]} draw outs.'