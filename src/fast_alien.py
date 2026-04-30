from alien import Alien

class FastAlien(Alien):
		"""Alienigena mais rápido que o normal."""

		def update(self):
			self.x += (self.settings.alien_speed * 2) * self.settings.fleet_direction
			self.rect.x = self.x