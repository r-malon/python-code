class Animal(object):
	def __init__(self, name, age=1):
		self.name = name
		self.age = age

class Dog(Animal):
	def __init__(self, name, age, breed):
		super().__init__(name, age)
		self.breed = breed


class Circle(object):
	def __init__(self, raio=1):
		self.raio = abs(raio)
	def area(self):
		return (raio ** 2) * 3.14159

class Point(object):
	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

class Square(object):
	def __init__(self, arg):
		pass


class State(object):
	def __init__(self, name, frontiers, cities):
		self.name = name
#		self.capital = capital
		self.frontiers = frontiers
		self.cities = cities

	def __eq__(self, other):
		return self.name == other.name

	def view_frontiers(self):
		while self.name in self.frontiers:
			self.frontiers.remove(self.name)
		return self.frontiers

	def shared_frontiers(self, other):
		shared = []
		for state in self.frontiers:
			if state in other.frontiers:
				shared.append(state)
		return shared

	def view_cities(self):
		names = []
		for city in self.cities:
			names.append(city.name)
		return names

	def rank_cities(self): # if false it starts from the lowest
		return sorted(
			self.cities, 
			key=lambda n: n.residents, 
			reverse=True
		)

class City:
	def __init__(self, name, residents, capital=False):
		self.name = name
		self.residents = residents
		self.capital = capital

if __name__ == '__main__':
	x = Dog('Rex', 18, 'German Shepherd')
	sc = State('Santa Catarina', ['Paraná', 'Rio Grande do Sul', 'Santa Catarina'], ['Blumenau', 'Floripa'])
	pr = State('Paraná', ['Santa Catarina'], 
		[
		City('Curitiba', 1000, capital=True), 
		City('Maringá', 200), City('Londrina', 300), 
		City('Pato Branco', 250)
		]
	)
	rs = State('Rio Grande do Sul', ['Santa Catarina'], ['Santa Maria', 'Pelotas', 'Chuí'])

	print(sc.view_frontiers())
	print(pr.view_cities())
	for n, city in enumerate(pr.rank_cities()):
		print(f'{n + 1} - {city.name}')
	print(pr.shared_frontiers(rs))
	print(sc == pr)
	print(rs.shared_frontiers(pr))
