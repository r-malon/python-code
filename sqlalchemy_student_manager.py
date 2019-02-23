from sqlalchemy import *
from sqlalchemy.ext import declarative
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative.declarative_base()

class Student(Base):
	__tablename__ = 'students'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(64), nullable=False)
	surname = Column(String(64), nullable=False)
	age = Column(Integer, nullable=False)
	#class_id = Column(ForeignKey("classes.id"))
	#average_grade = Column(Integer, nullable=False)

'''class Class(Base):
	__tablename__ = 'classes'
	id = Column(Integer, primary_key=True, autoincrement=True)
	leader = Column(String(64), nullable=False)
	student_number = Column(String(64), nullable=False) #remove?
	age = Column(Integer, nullable=False)
	students = relationship("Student")'''

class StudentManager:
	def __init__(self, db_name):
		self.engine = create_engine(r'sqlite:///C:\Users\RAFAEL\Videos\Python and other random things\' + db_name + '.db')
		self.DBsession = sessionmaker(bind=self.engine)
		self.session = self.DBsession()
		Base.metadata.create_all(self.engine)

	def search(self, name, surname):
		return self.session.query(Student).filter_by(name=name, surname=surname).first()

	def list_all(self, order):
		for student in self.session.query(Student).order_by(exec("Student." + order)).all():
			print(student.id, student.name, student.surname, student.age)

	def register(self, name, surname, age):
		name, surname = name.strip(" "), surname.strip(" ")
		if self.search(name, surname) is None:
			self.session.add(Student(name=name, surname=surname, age=age))
			self.session.commit()
			return True
		return False

	def delete(self, name, surname):
		try:
			self.session.delete(self.search(name, surname))
		except:
			return False
		self.session.commit()
		return True

	def update(self, name, surname, age):
		self.session.query(Student).update()

if __name__ == '__main__':
	manager = StudentManager('school')
	n = int(input("Number of students: "))
	for i in range(n):
		my_name = input("Name: ")
		my_surname = input("Surname: ")
		my_age = input("Age: ")
		print(manager.register(my_name, my_surname, my_age))
	print(manager.search('john', 'doe')) #put if True??
	ordering = input("Order by: ")
	manager.list_all(ordering)
	print(manager.delete('amando', 'silva'))