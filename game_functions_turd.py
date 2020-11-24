import sys
import pygame
from bullet import Bullet
from turd import Turd
from alien import Alien
from star import Star
from random import randint


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responding to keypresses."""
    # Move the ship to the left or right
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Responding to key releases."""
    # Stop moving the ship when releasing arrow keys.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, turd, stars):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # # Redraw all bullets behind ship and aliens.
    # for bullet in bullets.sprites():
    #     bullet.draw_bullet()
    #     # bullet.blitme() # change bullets to drops

    # Redraw ship
    ship.blitme()
    turd.blitme()

    # # Redraw fleet of aliens
    # aliens.draw(screen)

    # # Redraw group of turds
    # turds.draw(screen)

    # Redraw group of stars
    stars.draw(screen)

    # Make the most recently drawn screen visible.
    pygame.display.flip()


def check_turd_collisions(ai_settings, ship, turd):
    """Responding to turd-toilet collisions."""
    # Check collision y value
    collision_y = (ship.rect.bottom - 130) <= turd.rect.bottom
    # Check collision x value
    collision_x = (turd.rect.left >= ship.rect.left + 50) and (turd.rect.right <= ship.rect.right - 20)

    # Remove turd and create new turd after collision.
    if collision_y and collision_x:
        turd.create_new()
        ai_settings.turd_speed_factor += 1
        ai_settings.ship_speed_factor += 1


def update_turd(turd, stats):
    turd.check_bottom(stats)
    turd.update()


# def check_stars_edges(stars):
#     """Respond appropriately when stars/raindrops disappear off the bottom of the screen."""
#     for star in stars.sprites():
#         star.check_bottom()

# def check_turd_bottom(turd):
#     turd.check_bottom()

#
#
# def update_stars(stars):
#     """Update the position of all stars/raindrops."""
#     check_stars_edges(stars)
#     stars.update()


# def get_number_stars_x(ai_settings, star_width):
#     """Determine the number of stars that fit in a row."""
#     available_space_x = ai_settings.screen_width - 2 * star_width
#     number_stars_x = int(available_space_x / (2 * star_width))
#     return number_stars_x


# def get_number_rows_star(ai_settings, star_height):
#     """Determine the number of rows of stars that fit on the screen."""
#     number_rows = int(ai_settings.screen_height / (2 * star_height))
#     return number_rows


# def create_turds(ai_settings, screen, turds):
#     """Create a group of turds."""
#     turd = Turd(ai_settings, screen)
#     num_rows = get_num_rows_turd(ai_settings, turd.rect.height)
#
#     for row_number in range(num_rows):
#         create_turd(ai_settings, screen, turds, row_number)


# def create_star(ai_settings, screen, stars, row_number):
#     """Create a star and place it in a row."""
#     star = Star(ai_settings, screen)
#     star_width = star.rect.width
#
#     # Introduce randomness when placing stars
#     random_number = randint(-10, 10) # (-30, 30) for stars and *4 in row below
#     star.x = star_width + star_width * 2 * random_number
#     star.rect.x = star.x
#     star.rect.y = star.rect.height + 2 * star.rect.height * row_number
#     stars.add(star)


# def create_stars(ai_settings, screen, stars):
#     """Create a group of stars."""
#     star = Star(ai_settings, screen)
#     num_stars_x = get_number_stars_x(ai_settings, star.rect.width)
#     num_rows = get_number_rows_star(ai_settings, star.rect.height)
#
#     # Create stars
#     for row_number in range(num_rows):
#         for star_number in range(num_stars_x):
#             create_star(ai_settings, screen, stars, row_number)
