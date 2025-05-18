import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        old_radius = self.radius
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
           random_angle = random.uniform(20, 50)
           direction_1 = self.velocity.rotate(random_angle)
           direction_2= self.velocity.rotate(-random_angle)
           new_radius = old_radius - ASTEROID_MIN_RADIUS
           
           asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
           asteroid_1.velocity = direction_1 * 1.2
           asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
           asteroid_2.velocity = direction_2 * 1.2