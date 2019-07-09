from peewee import *

db = SqliteDatabase('peewee_test.db')

class BaseModel(Model):
	class Meta:
		database = db

class Student(BaseModel):
	name = CharField()
	surname = CharField()
	age = IntegerField()

class Receipe(BaseModel):
	name = CharField()

class Ingredient(BaseModel):
	name = CharField()
	receipe = ForeignKeyField(Receipe)

'''class Class(peewee.Mode):
	leader = peewee.CharField()
	class Meta:
		database = db'''
if __name__ == '__main__':
	db.connect()
	db.create_tables([Student, Receipe, Ingredient])
	bolo = Receipe.create(name='bolo de laranja')
	Ingredient.create(name='farinha', receipe=bolo)
	Ingredient.create(name='ovo', receipe=bolo)
	Ingredient.create(name='laranja', receipe=bolo)
	for i in Ingredient.select().where(Ingredient.receipe.name == 'bolo'):
		print(i.name)