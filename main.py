import pygame
from vector import *
from fish import *
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

#Fish list
fish_list = []
for _ in range(15): 
    random_position = Vector(random.randint(0, 750), random.randint(0, 550))  #Sørger for at fiskene starter inden for skærmen
    fish = Fish(screen)
    fish.position = random_position
    fish_list.append(fish)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 128, 255))

    for fish in fish_list:
        fish.update()
        fish.draw()
    
    pygame.display.flip()
    clock.tick(240)

pygame.quit()
