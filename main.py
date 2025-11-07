# This allows us to use code from the open-source
# pygame library throughout this file
import pygame
from constants import *
from logger import log_state
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
        pygame.display.flip()
        clock.tick(60)
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()
