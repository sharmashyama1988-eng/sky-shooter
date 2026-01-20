import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 128, 255))  # Blue
        self.rect = self.image.get_rect(center=(screen_width / 2, screen_height - 50))
        self.speed = 6
        self.fire_rate = 200  # milliseconds
        self.last_shot = pygame.time.get_ticks()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, keys, all_sprites, projectiles):
        # Movement
        move_vector = pygame.math.Vector2()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            move_vector.x -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            move_vector.x += 1
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            move_vector.y -= 1
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            move_vector.y += 1
        
        if move_vector.length_squared() > 0:
            move_vector.normalize_ip()
            self.rect.move_ip(move_vector * self.speed)

        # Keep player on screen
        self.rect.clamp_ip(pygame.Rect(0, 0, self.screen_width, self.screen_height))

        # Firing
        if keys[pygame.K_SPACE] or pygame.mouse.get_pressed()[0]:
            self.try_fire(all_sprites, projectiles)

    def try_fire(self, all_sprites, projectiles):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.fire_rate:
            self.last_shot = now
            # Fire a projectile upwards from the player's center
            projectile = Projectile(self.rect.centerx, self.rect.top, -10)
            all_sprites.add(projectile)
            projectiles.add(projectile)
