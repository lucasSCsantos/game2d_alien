import sys
import pygame

from alien_invasion_refactored import AlienInvasion
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



if __name__ == "__main__":
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()
