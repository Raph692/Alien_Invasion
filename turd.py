import pygame
from pygame.sprite import Sprite
from random import randint
from time import sleep


class Turd(Sprite):
    """A class to represent a turd."""

    def __init__(self, ai_settings, screen):
        """Initialize the turd and set its starting position."""
        super(Turd, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the turd image and set its rect attribute.
        self.image = pygame.image.load('images/turd.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new turd at a random location at the top of the screen.
        random_num = randint(0, 1200) # screen width
        self.rect.left = self.screen_rect.left + random_num
        self.rect.y = self.screen_rect.top

    def blitme(self):
        """Draw the turd at its current location."""
        self.screen.blit(self.image, self.rect)

    def create_new(self):
        """Create new turd at the top of the screen."""
        screen_rect = self.screen.get_rect()
        random_num = randint(0, 1200)  # screen width
        self.rect.y = screen_rect.top
        self.rect.x = self.screen_rect.left + random_num

    def check_bottom(self, stats):
        """Move row of stars/raindrops to the top if they disappear off the bottom of the screen."""
        if stats.ships_left > 0:
            screen_rect = self.screen.get_rect()
            if self.rect.y >= screen_rect.bottom:
                stats.ships_left -= 1
                self.create_new()
        else:
            stats.game_active = False

    def update(self):
        """Move the turd downwards."""
        self.rect.y += self.ai_settings.turd_speed_factor
