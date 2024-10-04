import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
        self.velocity = pygame.math.Vector2(0, 0)
        #print(f"asteroid created at: {self.x}, {self.y}")

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt