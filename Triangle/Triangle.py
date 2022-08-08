class Triangle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		if not self.isValid():
			raise InvalidTriangleException('Triângulo inválido')
	def __str__(self):
		return f'''\
A: {self.a}; B: {self.b}; C: {self.c}
Perímetro: {self.getPerimeter()}
Area: {self.getArea()}
Tipo: {self.getType()}\
'''
	def __eq__(self, other):
		return other.a in {self.a, self.b, self.c} \
		  and other.b in {self.a, self.b, self.c} \
		  and other.c in {self.a, self.b, self.c}
	def __lt__(self, other):
		return self.getArea() < other.getArea()
	def __gt__(self, other):
		return self.getArea() > other.getArea()
	def getType(self):
		return 'Escaleno' if self.a != self.b != self.c else \
		  'Equilátero' if self.a == self.b == self.c else 'Isósceles'
	def getPerimeter(self):
		return self.a + self.b + self.c
	def getArea(self):
		s = self.getPerimeter() / 2
		return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
	def isValid(self):
		return self.a + self.b >= self.c \
		  and self.a + self.c >= self.b \
		  and self.b + self.c >= self.a

class InvalidTriangleException(Exception):
	'''Invalid triangle'''
