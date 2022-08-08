import unittest
from Triangle import *

# docs.python.org/3/library/unittest.html

class TestTriangle(unittest.TestCase):
	def setUp(self):
		self.tri = Triangle(15, 13, 4)
	def test_eq(self):
		self.assertEqual(Triangle(4, 3, 5), Triangle(5, 4, 3))
		self.assertTrue(Triangle(4, 3, 5) == Triangle(5, 3, 4))
	def test_lt(self):
		self.assertLess(Triangle(4, 3, 5), self.tri)
	def test_gt(self):
		self.assertGreater(self.tri, Triangle(5, 3, 4))
	def test_area(self):
		self.assertEqual(self.tri.getArea(), 24)
	def test_peri(self):
		self.assertEqual(self.tri.getPerimeter(), 32)
	def test_type(self):
		self.assertEqual(self.tri.getType(), 'Escaleno')
		self.tri.a, self.tri.b, self.tri.c = 5, 5, 5
		self.assertEqual(self.tri.getType(), 'Equilátero')
		self.tri.a, self.tri.b, self.tri.c = 5, 5, 6
		self.assertEqual(self.tri.getType(), 'Isósceles')
	def test_invalid(self):
		with self.assertRaises(InvalidTriangleException):
			self.tri = Triangle(20, 1, 1)

if __name__ == '__main__':
	unittest.main()
