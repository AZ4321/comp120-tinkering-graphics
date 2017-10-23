import pygame
pygame.init()

##This code is responsible for creating the window and keeping it there
window_height = 800
window_width = 400
window = pygame.display.set_mode([window_height, window_width])
running = 1
screen = window;

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0

##This is responsible for the image/surface loading
image = pygame.image.load('monster.jpg')
screen.blit(image,(20,20))

surface = pygame.Surface((500, 500))

pygame.display.flip()


