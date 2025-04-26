from pygame import *
from random import randint
from time import time as timer
import random 

# нам потрібні такі картинки:
img_back = "doroga.jpg"  # фон гри
img_car = "car.png"  # герой
img_enemy = "polisecar.png"  # ворог


# створюємо віконце
win_width = 700
win_height = 500
display.set_caption("Перегони")
win = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back),
                             (win_width, win_height))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,  # один рядок
                 size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(  # один рядок
            image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


# Класс машины
class Car(GameSprite):
    def __init__(self, player_image, size_x, size_y):
        super().__init__(player_image, win_width // 2, win_height - size_y - 10,  size_x, size_y, 5)


class PlayerCar(Car):
    def __init__(self, player_image, size_x, size_y):
        super().__init__(player_image, size_x, size_y)
        self.left = False
        self.right = False

    def move(self):
        # for obs in obstacles:
        #     if abs(self.rect.y - obs.y) < 150 and obs.x < self.rect.x + self.win_width and obs.x + obs.win_width > self.rect.x:
        #         if self.rect.x > win_width // 2:
        #             self.rect.x -= self.speed
        #         else:
        #             self.rect.x += self.speed
        if self.left:
            self.rect.x -= 5
        if self.right:
            self.rect.x += 5


class Background(GameSprite):
    def move(self, speed):
        self.rect += speed
        if self.rect.y > win_height:
            self.rect.y = -win_height


# Класс препятствий
class Obstacle:
    def __init__(self):
        self.win_width = 50
        self.height = 50
        self.x = random.randint(0, win_width - self.win_width)
        self.y = -self.height
        self.speed = 5

    def draw(self, win):
        draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

# Основной цикл игры
def main():
    run = True
    clock = time.Clock()
    car = PlayerCar(img_car, 50, 100)
    bg_1 = Background(img_back, 0, 0, win_width, win_height, car.speed)
    bg_2 = Background(img_back, 0, -win_height, win_width, win_height, car.speed)
    # obstacles = [Obstacle()]

    while run:
        clock.tick(60)
        win.fill((255, 255, 255))

        for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    car.left = True
                if e.key == K_RIGHT:
                    car.right = True
            if e.type == KEYUP:
                if e.key == K_LEFT:
                    car.left = False
                if e.key == K_RIGHT:
                    car.right = False



        # Движение машины и препятствий
        car.move()
        # for obs in obstacles:
        #     obs.move()
        #     if obs.y > win_height:
        #         obstacles.remove(obs)
        #         obstacles.append(Obstacle())

        # Отрисовка
        car.update()
        car.reset()

        # for obs in obstacles:
        #     obs.draw(win)

        display.update()

    quit()

if __name__ == "__main__":
    main()
