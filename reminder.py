import ctypes
import winsound as ws
import time

class Reminder:
	def __init__(self, msg, hour, minute, second=0, sound='SystemExclamation',
	 repeatable=False):
		self.date = [hour, minute, second]
		self.sound = sound
		self.msg = msg
		self.repeatable = repeatable
		self.active = True

	#@staticmethod
	def reminder(self):
		ws.PlaySound(self.sound, ws.SND_ALIAS)
		ctypes.windll.user32.MessageBoxW(0, self.msg, "Reminder!", 0)

	def main(self):
		while True:
			if self.date == list(time.localtime())[3:6]:
				self.reminder()
				if not self.repeatable:
					break

if __name__ == '__main__':
	hour = int(input('Hour: '))
	minute = int(input('Minute: '))
	second = int(input('Second: '))
	x = Reminder('Go shopping!', hour, minute, second, 'alert.mp3')
	x.main()