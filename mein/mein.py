from pygame import *
from random import randint
from time import time as timer # ⬅️

# нам потрібні такі картинки:
img_back = "doroga.jpg"  # фон гри
img_hero = "car.png"  # герой
img_enemy = "polisecar.png"  # ворог


# створюємо віконце
win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back),
                             (win_width, win_height))


import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры экрана
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Машина объезжает препятствия")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Класс машины
class Car:
    def __init__(self):
        self.width = 50
        self.height = 60
        self.x = WIDTH // 2
        self.y = HEIGHT - self.height - 10
        self.speed = 5

    def draw(self, win):
        pygame.draw.rect(win, BLUE, (self.x, self.y, self.width, self.height))

    def move(self, obstacles):
        for obs in obstacles:
            if abs(self.y - obs.y) < 150 and obs.x < self.x + self.width and obs.x + obs.width > self.x:
                if self.x > WIDTH // 2:
                    self.x -= self.speed
                else:
                    self.x += self.speed

# Класс препятствий
class Obstacle:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = random.randint(0, WIDTH - self.width)
        self.y = -self.height
        self.speed = 5

    def draw(self, win):
        pygame.draw.rect(win, RED, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

# Основной цикл игры
def main():
    run = True
    clock = pygame.time.Clock()
    car = Car()
    obstacles = [Obstacle()]

    while run:
        clock.tick(60)
        win.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Движение машины и препятствий
        car.move(obstacles)
        for obs in obstacles:
            obs.move()
            if obs.y > HEIGHT:
                obstacles.remove(obs)
                obstacles.append(Obstacle())

        # Отрисовка
        car.draw(win)
        for obs in obstacles:
            obs.draw(win)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
              
