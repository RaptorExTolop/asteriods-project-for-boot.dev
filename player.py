import pygame
from circleshape import *
from constants import *
from bullet import *

class Player(CircleShape):
    def __init__(self, x, y, shot_groups):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 180
        self.image = pygame.Surface((PLAYER_RADIUS*2, PLAYER_RADIUS*2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.shot_groups = shot_groups

    def draw(self, Screen):
        pygame.draw.polygon(Screen, "white", self.triangle(), width=3)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        new_shot = Shot(self.position.x, self.position.y, velocity * PLAYER_SHOOT_SPEED)
        for group in self.shot_groups:
            group.add(new_shot)

    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            if keys[pygame.K_LSHIFT]:
                self.move(dt)
            self.move(dt)
        if keys[pygame.K_s]:
            if keys[pygame.K_LSHIFT]:
                self.move(-dt)
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.rect.center = self.position

        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]