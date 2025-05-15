import pygame
from constants import *
from player import Player


def main():
    pygame.init()

    # STARTING VARIABLES
    play = True
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    print(f"""
        Starting Asteroids!
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}
          """)

    # GAME LOOP
    while play:

        # window exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # PLAYER CONFIG    
        ship.update(dt)
        
        # RENDER
        screen.fill("black")
        ship.draw(screen) # after screen fill -> before screen flip
        pygame.display.flip()

        # framerate (60 FPS)
        dt = clock.tick(60) / 1000

if (__name__ == "__main__"):
    main()