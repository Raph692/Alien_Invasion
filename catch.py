import pygame
from settings import Settings
from ship import Ship
from turd import Turd
from game_stats import GameStats
import game_functions_turd as gf
from pygame.sprite import Group


def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    # Create settings instance
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Catch the turd!")

    # Make an instance to store game statistics
    stats = GameStats(ai_settings)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    turd = Turd(ai_settings, screen)
    bullets = Group()
    # aliens = Group()
    stars = Group()

    # # Create the fleet of aliens.
    # gf.create_fleet(ai_settings, screen, ship, aliens)

    # # Create stars
    # gf.create_stars(ai_settings, screen, stars)

    # Start the main loop for the game.
    while True:

        # Respond to keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            # turd.update()

            # Update bullets positions and get rid of old bullets.
            # gf.update_bullets(bullets)
            # gf.check_bullet_alien_collisions(ai_settings, screen, ship, bullets, aliens)
            # gf.check_turd_collisions(ai_settings, screen, ship, turd)
            gf.check_turd_collisions(ai_settings, ship, turd)
            gf.update_turd(turd, stats)
            # gf.update_aliens(ai_settings, aliens)
            # gf.update_stars(stars)

        # Update images on the screen and flip to the new screen.
        gf.update_screen(ai_settings, screen, ship, turd, stars)


run_game()
