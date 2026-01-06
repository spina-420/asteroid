import pygame
import sys
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
 
def main():
    
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
                 
    asteroid_field = AsteroidField()
    
    player_ship = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
   
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")

        updatable.update(dt)
        
        for _ in asteroids:
            if _.collides_with(player_ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                
        for _ in asteroids:
            for shot in shots:
                if _.collides_with(shot):
                    _.split()
                    shot.kill()
                    log_event("asteroid_shot")
                
        for _ in drawable:
            _.draw(screen)
        
        
        dt = clock.tick(60) / 1000
        pygame.display.flip()
        


if __name__ == "__main__":
    main()
