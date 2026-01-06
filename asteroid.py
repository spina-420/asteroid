import pygame
import random
from circleshape import CircleShape
from constants import *
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def update(self, dt):
        self.position += self.velocity * dt
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_rad = self.radius - ASTEROID_MIN_RADIUS
            ass1 = Asteroid(self.position[0], self.position[1], new_rad)
            ass2 = Asteroid(self.position[0], self.position[1], new_rad)
            ass1.velocity = self.velocity.rotate(random.uniform(20, 50)) * 1.2
            ass2.velocity = self.velocity.rotate(random.uniform(-20, -50)) * 1.2
