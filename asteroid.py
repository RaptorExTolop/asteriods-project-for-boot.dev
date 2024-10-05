import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        #print(f"asteroid created at: {self.x}, {self.y}")

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
    
    def split(self, asteroid_groups):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vel1 = self.velocity.rotate(random_angle) * 1.2
            vel2 = self.velocity.rotate(-random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_one.velocity = vel1
            new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_two.velocity = vel2