import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()

    # STARTING VARIABLES
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()
    

    print(f"""
        Starting Asteroids!
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}
          """)

    # GAME LOOP
    while True:

        # window exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # PRE-RENDER    
        updatable.update(dt)
        
        # Condition check
        for asteroid in asteroids:
            if asteroid.collision_check(ship):
                print("""
                      GAME OVER!
                        """)
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
        
        # RENDER
        screen.fill("black")

        for shape in drawable:
            shape.draw(screen) # after screen fill -> before screen flip
        
        pygame.display.flip()

        # framerate (60 FPS)
        dt = clock.tick(60) / 1000

if (__name__ == "__main__"):
    main()