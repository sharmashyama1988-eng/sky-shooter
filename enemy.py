import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.health = 3
        self.score_value = 100

    def update(self):
        self.rect.y += self.speed

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
            return True
        return False
