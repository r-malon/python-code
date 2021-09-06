from reminder import Reminder
from threading import Thread

class ReminderManager:
	def __init__(self):
		self.reminders = []

	def create(self):
		msg = input('What do you want to remind: ')
		hour = int(input('Hour: '))
		minute = int(input('Minute: '))
		second = int(input('Second: '))
		self.reminders.append(Reminder(msg, hour, minute, second))

	def list_all(self):
		for i in enumerate(self.reminders):
			print(str(i[0] + 1) + ' > ' + i[1].msg + f" - {i[1].date[0]}:{i[1].date[1]}:{i[1].date[2]}")

	def delete(self):
		n = int(input('Type the id you will delete: '))
		try:
			if n <= 0:
				raise IndexError
			del self.reminders[n-1]
		except IndexError:
			print('Enter a valid id!')

	def activate(self):
		n = int(input('Type the id of the reminder you will (de)activate: '))
		try:
			if n <= 0:
				raise IndexError
			self.reminders[n-1].active = not self.reminders[n-1].active
		except IndexError:
			print('Enter a valid id!')

	def main(self):
		for i in self.reminders:
			x = Thread(target=i.main)
			x.start()


if __name__ == '__main__':
	manager = ReminderManager()
	n = int(input("How many reminders you will create? "))
	for i in range(n):
		manager.create()
	manager.list_all()
	manager.delete()
	manager.list_all()
	manager.activate()
	manager.main()
