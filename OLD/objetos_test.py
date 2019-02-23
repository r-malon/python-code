class player:
        life = 100
        def __init__(self, name):
                self.name = name
                money = 10000
        def buy(self, gun):s
                money -= gun.price
        def shot(self):
                life -= dmg*hits
class gun:
	def __init__(self, dmg, price, ammo):
		self.dmg = dmg
		self.price = price
		self.ammo = ammo
	def hit(self, player, shots):
                        player.life -= shots * dmg
                        ammo -= shots
                        if player.life == 0:
                                print('vc matou %s' % player.name)
nome = int(input('digite seu nome: '))
nome = player(nome)
ak-47 = gun(35, 2500, 30)
