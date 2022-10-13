import pygame
from setting import Settings
import sys
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Inititialize the game, and create game resources"""
        pygame.init()
        self.setting = Settings()

        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)


    def run_game(self):
        """Start the main loop for the the game"""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.setting.bg_color)

            self.ship.blitme()

            pygame.display.flip()

if __name__ == "__main__":
    # make game instance and run game
    ai = AlienInvasion()
    ai.run_game()

