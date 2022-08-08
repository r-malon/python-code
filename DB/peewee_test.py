from peewee import *

db = SqliteDatabase('peewee_test.db')

class BaseModel(Model):
	class Meta:
		database = db

class Student(BaseModel):
	name = CharField()
	surname = CharField()
	age = IntegerField()

class Recipe(BaseModel):
	name = CharField()

class Ingredient(BaseModel):
	name = CharField()
	Recipe = ForeignKeyField(Recipe)

'''
class Class(peewee.Mode):
	leader = peewee.CharField()
	class Meta:
		database = db
'''
if __name__ == '__main__':
	db.connect()
	db.create_tables([Student, Recipe, Ingredient])
	bolo = Recipe.create(name='bolo de laranja')
	Ingredient.create(name='farinha', Recipe=bolo)
	Ingredient.create(name='ovo', Recipe=bolo)
	Ingredient.create(name='laranja', Recipe=bolo)
	for i in Ingredient.select().where(Ingredient.Recipe.name == 'bolo'):
		print(i.name)
