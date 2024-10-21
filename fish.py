from turtle import Screen
import pygame
from vector import Vector


velocity = Vector(1,1)
position = Vector(400,300)


class Fish:
    def __init__(self, screen):
        self.fish_img = pygame.image.load('Fish.png')
        self.fish_img = pygame.transform.scale(self.fish_img, (50,50))
        self.velocity = Vector(1,1)
        self.position = Vector(400,300)
        self.screen = screen


    def update(self, ):
        self.velocity = self.screenConfinement()
        self.position += self.velocity
        #print(self.position) #Tjek position for fejl



        
    def draw(self,):
        self.screen.blit(self.fish_img,(self.position.x,self.position.y))

        
    def screenConfinement(self,):
        velocity = self.velocity
        if self.position.x < 2 or self.position.x > self.screen.get_width() - self.fish_img.get_width() - 2:
            velocity.x *= -1
        if self.position.y < 2 or self.position.y > self.screen.get_height() - self.fish_img.get_height() - 2:
            velocity.y *= -1
        return velocity 
