import pygame
import sys

class GameEventHandler:
    """Responsavel apenas por ler e tratar os eventos do teclao/janela"""
    def __init__(self, ship, bullt_manager):
        self.ship = ship
        self.bullet_manager = bullt_manager

    def _check_events(self):
        """Responde a eventos de pressionamento de teclas e de mouse."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif (
                event.type == pygame.KEYDOWN
            ):
                self._handle_keydown(event) 
            elif event.type == pygame.KEYUP: 
                self._handle_keyup(event)
    
    def _handle_keydown(self, event) -> None:
        """Responde a eventos de pressionamento de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.bullet_manager.fire_bullet()

    def _handle_keyup(self, event) -> None:
        """Responde a eventos de liberação de teclas."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
