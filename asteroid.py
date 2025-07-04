import pygame
from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
     def __init__(self,x,y,radius):
          super().__init__(x,y,radius)
     
     def draw(self, screen):
          pygame.draw.circle(screen,(255,255,255),self.position, self.radius,2)
     
     def update(self,dt):
          forward = pygame.Vector2(0, 1)
          self.position += self.velocity * dt

     def split(self):
          self.kill()
          if self.radius <= ASTEROID_MIN_RADIUS:
               return
          angle = random.uniform(20,50)
          vector1 = self.velocity.rotate(angle)
          vector2 = self.velocity.rotate(-angle)
          radius = self.radius - ASTEROID_MIN_RADIUS
          asteroid1 = Asteroid(self.position.x,self.position.y,radius)
          asteroid1.velocity = (self.velocity + vector1) * 1.2
          asteroid2 = Asteroid(self.position.x,self.position.y,radius)
          asteroid2.velocity = (self.velocity + vector2) * 1.2