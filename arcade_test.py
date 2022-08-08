import arcade

class MyGame(arcade.Window):
	def __init__(self, w, h):
		super().__init__(w, h)
		self.paused = False
	def setup(self):
		self.kills = 0
		self.sprite_list = arcade.SpriteList()
		self.wall_list = []
		self.player_sprite = arcade.Sprite("pepe.png")
		self.sprite_list.append(self.player_sprite)
		self.phys_engine = arcade.PhysicsEngineSimple(
			self.player_sprite, 
			self.sprite_list
		)
	def on_draw(self):
		arcade.start_render()
		self.sprite_list.draw()
	def update(self):
		self.phys_engine.update()

if __name__ == '__main__':
	game = MyGame(800, 600)
	game.setup()
	arcade.run()
