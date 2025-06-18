import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    """docstring for ."""
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20,50)
        velocity_new1 = self.velocity.rotate(random_angle)
        velocity_new2 = self.velocity.rotate (-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid1.velocity = velocity_new1 * 1.2
        asteroid2.velocity = velocity_new2 * 1.2
