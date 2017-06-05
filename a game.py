import pygame


def main():
    """Set up the game and tun the main game loop"""
    pygame.init()
    surface_sz = 480

    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    small_rect = (300, 200, 150, 90)
    color = (255, 0, 0)  # Red

    while True:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break

        main_surface.fill((0, 200, 255))

        main_surface.fill(color, small_rect)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
