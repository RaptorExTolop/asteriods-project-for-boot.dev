import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # initialises pygame
    pygame.init()

    # Game time and delta time
    game_time = pygame.time.Clock()
    dt = 0

    # creates 4 groups to make updating and drawing easier
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # adds player to the drawable and update group
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, (shots, drawable, updatable))

    # asteriods container bullshit
    Asteroid.containers = (asteroids, updatable, drawable)

    # asteroid field colourful 4 letter words
    AsteroidField.containers = (updatable,)
    asteriod_field = AsteroidField()
    

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

        for asteroid in asteroids:
            if player.collide(asteroid):
                print("Game Over!")
                sys.exit()


        pygame.display.flip()
        dt = game_time.tick(60) / 1000


# no idea what this does -_-
if __name__ == "__main__":
    main()