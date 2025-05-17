import pygame
import random
from time import time as timer

# Ініціалізація
pygame.init()
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 30)
img_back = "doroga.jpg"  # фон гри

# Кольори
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
GRAY = (50, 50, 50)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  # один рядок
                 size_x, size_y, player_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(  # один рядок
            pygame.image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Background(GameSprite):
    def move(self, speed):
        self.rect.y += speed
        if self.rect.y > HEIGHT:
            self.rect.y = -HEIGHT

# Гравець
player = pygame.Rect(WIDTH//2 - 20, HEIGHT - 80, 40, 60)
player_img = pygame.transform.scale(pygame.image.load("car.png"), (player.width, player.height))
player_speed = 5
points = 0
now_time = timer()


bg_1 = Background(img_back, 0, 0, WIDTH, HEIGHT, player_speed)
bg_2 = Background(img_back, 0, -HEIGHT, WIDTH, HEIGHT, player_speed)

# Ворожі машини
enemy_speed = 4
enemies = []
enemies_img = []
spawn_timer = 0

# Ігровий цикл
running = True
while running:
    bg_1.move(2)
    bg_1.reset()
    bg_2.move(2)
    bg_2.reset()
    screen.blit(player_img, (player.x, player.y))
    # pygame.draw.rect(screen, BLUE, player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рух гравця
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Спавн ворогів
    spawn_timer += 1
    if spawn_timer >= 30:
        enemy_x = random.randint(0, WIDTH - 40)
        enemy = pygame.Rect(enemy_x, -60, 40, 60)
        police_img = pygame.transform.scale(pygame.image.load("polisecars.png"), (enemy.width, enemy.height))
        enemies.append(enemy)
        enemies_img.append(police_img)
        spawn_timer = 0




    # Рух ворогів
    for i in range(len(enemies)):
        enemies[i].y += enemy_speed
        # pygame.draw.rect(screen, RED, enemies[i])
        screen.blit(enemies_img[i], (enemies[i].x, enemies[i].y))

        # Колізія
        if player.colliderect(enemies[i]):
            text = font.render("Аварія!", True, WHITE)
            screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        # Видалити ворогів, які вийшли за екран
        if enemy.top > HEIGHT:
            enemies.remove(enemies[i])

        text_points = font.render("Бали: " + str(points), True, WHITE)
        screen.blit(text_points, (20, 20))
        points = int(timer() - now_time)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
