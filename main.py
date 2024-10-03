import pygame
from constants import *
from player import *

def main():
    # initialises pygame
    pygame.init()

    # Game time and delta time
    game_time = pygame.time.Clock()
    dt = 0

    # creates 2 groups to make updating and drawing easier
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # adds player to the drawable and update group
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # screen size
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # makes file quitable
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quiting!")
                return
        
        screen.fill((0, 0, 0))

        # updates and draws automaticly  
        for item in updatable:
            item.update(dt)
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = game_time.tick(60) / 1000


# no idea what this does -_-
if __name__ == "__main__":
    main()