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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000

        

        


if __name__ == "__main__":
    main()
