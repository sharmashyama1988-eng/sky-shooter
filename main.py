import pygame
import random
from player import Player
from enemy import Enemy
from projectile import Projectile

# 1. Initialize Pygame
pygame.init()

# 2. Screen Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Space Shooter")

# 3. Colors & Fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.Font(None, 36)

# 4. Game Variables
score = 0
game_over = False
clock = pygame.time.Clock()
FPS = 60

# 5. Sprite Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Create Player
player = Player(SCREEN_WIDTH, SCREEN_HEIGHT)
all_sprites.add(player)

# Enemy Spawning Timer
ENEMY_SPAWN_RATE = 1000  # milliseconds
last_enemy_spawn = pygame.time.get_ticks()

def spawn_enemy():
    x = random.randint(50, SCREEN_WIDTH - 50)
    y = -50
    enemy = Enemy(x, y, speed=random.randint(2, 4))
    all_sprites.add(enemy)
    enemies.add(enemy)

# 6. Game Loop
running = True
while running:
    # 7. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        # 8. Update Sprites
        keys = pygame.key.get_pressed()
        player.update(keys, all_sprites, projectiles)
        
        # Spawn new enemies
        now = pygame.time.get_ticks()
        if now - last_enemy_spawn > ENEMY_SPAWN_RATE:
            last_enemy_spawn = now
            spawn_enemy()
            
        enemies.update()
        projectiles.update()

        # 9. Collision Detection
        # Projectiles hitting enemies
        hits = pygame.sprite.groupcollide(projectiles, enemies, True, False)
        for proj, hit_enemies in hits.items():
            for enemy in hit_enemies:
                if enemy.take_damage(proj.damage):
                    score += enemy.score_value
                    # You could add an explosion animation here
                
        # Enemies hitting player
        if pygame.sprite.spritecollide(player, enemies, False):
            game_over = True # End the game if an enemy touches the player

        # Remove enemies that go off-screen
        for enemy in list(enemies):
            if enemy.rect.top > SCREEN_HEIGHT:
                enemy.kill()

    # 10. Drawing / Rendering
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Display Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    if game_over:
        game_over_text = font.render("GAME OVER", True, WHITE)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(game_over_text, text_rect)

    # 11. Flip the display
    pygame.display.flip()

    # 12. Control Framerate
    clock.tick(FPS)

# 13. Quit Pygame
pygame.quit()
