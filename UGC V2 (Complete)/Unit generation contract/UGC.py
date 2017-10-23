import pygame
import random
from random import randint

pygame.init()

##This code is responsible for the window and the random monster generator
window_height = 800
window_width = 400
window = pygame.display.set_mode([window_height, window_width])
screen = window;

imageone = pygame.image.load('monster1.jpg')
imagetwo = pygame.image.load('monster2.jpg')
imagethree = pygame.image.load('monster3.jpg')
imagefour = pygame.image.load('monster4.jpg')

monsterimage = [imageone, imagetwo, imagethree, imagefour]
imagetype = random.choice(monsterimage)
screen.blit(imagetype, (20, 20))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



