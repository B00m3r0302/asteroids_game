# This allows us to use code from the open-source
# pygame library throughout this file
import pygame
from constants import *
from logger import log_state
from player import *
def main():
    print("Starting Asteroids!\nScreen width: 1280\nScreen height: 720")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
        player1.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

        

        


if __name__ == "__main__":
    main()
