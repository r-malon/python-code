import peewee

db = peewee.SqliteDatabase('peewee_test.db')

class Student(peewee.Model):
	name = peewee.CharField()
	surname = peewee.CharField()
	age = peewee.IntegerField()
	class Meta:
		database = db

'''class Class(peewee.Mode):
	leader = peewee.CharField()
	class Meta:
		database = db'''
if __name__ == '__main__':
	db.connect()
	db.create_tables([Student])
	x = Student.create(name='zeze', surname='silva', age=52)
	x.save()