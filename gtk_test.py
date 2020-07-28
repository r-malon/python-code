import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
	def __init__(self, title):
		self.title = title
		Gtk.Window.__init__(self, title=self.title)
		self.box = Gtk.Box(spacing=0)
		self.btn_list = []
		self.add(self.box)
		for i in range(10):
			self.btn_list.append(Gtk.Button(label=str(i)))
			self.btn_list[i].connect('clicked',
			 lambda: print(self.btn_list[i].get_label()))
			self.box.pack_start(self.btn_list[i], 1, 1, 20)
		
if __name__ == '__main__':
	win = MyWindow('hello!')
	win.connect("destroy", Gtk.main_quit)
	win.set_default_size(600, 480)
	win.set_icon_from_file('fallout.ico')
	win.show_all()
	Gtk.main()