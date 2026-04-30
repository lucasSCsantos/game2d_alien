import sys
import pygame

from settings import Settings
from ship import Ship

from bullet_manager import BulletManager
from fleet_manager import FleetManager
from game_renderer import GameRenderer
from game_events import GameEventHandler

from fast_alien import FastAlien
from alien import Alien

class AlienInvasion:
    """Gerencia os recursos e o comportamento do jogo."""

    def __init__(self):
        """Inicializa o jogo e cria os recursos do jogo."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self.screen, self.settings)
        
        self.bg_color = self.settings.bg_color

        self.bullet_manager = BulletManager(self.screen, self.settings, self.ship)
        self.fleet_manager = FleetManager(self.screen, self.settings, self.ship, FastAlien)
        self.event_handler = GameEventHandler(self.ship, self.bullet_manager)
        self.renderer = GameRenderer(self.screen, self.bg_color, self.ship, self.fleet_manager.aliens, self.bullet_manager.bullets)

       

    def _update_game_state(self):
        """Atualiza os elementos do jogo para refletir as mudanças ocorridas."""
        self.ship.update()
        self.bullet_manager._update_bullets(self.fleet_manager.aliens)
        self.fleet_manager._update_aliens()

    def run_game(self):
        """Cria um laço de repetição para a tela sempre ficar visível até que o usuário feche a janela"""
        self.fleet_manager.create_fleet()

        while True:
            self.event_handler._check_events()
            self._update_game_state()
            self.renderer._render_screen()

if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()