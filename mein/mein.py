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
