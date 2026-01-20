import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill((255, 255, 0))  # Yellow
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.damage = 1
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 5000  # 5 seconds in milliseconds

    def update(self):
        self.rect.y += self.speed
        if pygame.time.get_ticks() - self.spawn_time > self.lifetime:
            self.kill()
