import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        l_vector = self.velocity.rotate(-random_angle)
        r_vector = self.velocity.rotate(random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        l_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        l_asteroid.velocity = l_vector * 1.2
        r_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        r_asteroid.velocity = r_vector * 1.2
