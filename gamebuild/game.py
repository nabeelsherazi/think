import sys
sys.path.append('..\\..\\my lib')
from pointclass import *
import pygame
import time


def main():
    """Setup the game and run the main game loop"""
    pygame.init()
    surface_sz = 480

    main_surface = pygame.display.set_mode((surface_sz, surface_sz))
    # Takes a tuple describing size of surface in x, y

    small_rect = (300, 200, 150, 90)  # Corner x, corner y, length, height
    color1 = (255, 0, 0)
    color2 = (0, 200, 255)

    ball = pygame.image.load("img\\ball.png")

    # Instantiate a font object
    my_font = pygame.font.SysFont("Courier", 16)

    # FPS counter
    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        # Update game and data structures here

        # Update FPS counter here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1 - t0)
            t0 = t1


        # Everything is drawn from scratch on each frame

        main_surface.fill(color2)  # Background

        main_surface.fill(color1, small_rect)

        main_surface.blit(ball, (100, 120))

        the_text = my_font.render("Frame {0}, average {1:.1f} fps"
                                  .format(frame_count, frame_rate), True, (0, 0, 0))
        main_surface.blit(the_text, (10, 10))

        # Display
        pygame.display.flip()

    pygame.quit()

main()
