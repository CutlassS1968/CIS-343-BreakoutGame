import pygame as pg
from random import randint
from random import seed
import math

# Is a subclass of pygame.sprite.Sprite.
#
# As talked about in class, each subclass of pygame.sprite.Sprite will have a draw() and update() method.
# You will need to override the update() method for anything that moves.
#
# The image will be a circle.
#
# The balls will bounce off walls, the paddle, and bricks.
#
# When a ball bounces off a brick, the brick will receive damage if 25.
class Ball(pg.sprite.Sprite):

  def __init__(self):
    pg.sprite.Sprite.__init__(self)

    # Initialize ball variables
    self.image = pg.Surface([20, 20])
    self.image.fill((0, 0, 0))
    self.rect = self.image.get_rect()
    self.collision = False
    self.speed = 4
    self.x = 400
    self.y = 500
    self.direction = randint(0, 360)


  def bounce(self, diff):
    self.direction = (180 - self.direction) % 360
    self.direction -= diff


  def update(self):
    dir_radians = math.radians(self.direction)

    self.x += self.speed * math.sin(dir_radians)
    self.y -= self.speed * math.cos(dir_radians)

    self.rect.x = self.x
    self.rect.y = self.y

    # if ball hits top wall
    if self.y <= 0:
      self.bounce(0)
      self.y = 1

    # if ball hits left side wall
    if self.x <= 0:
      self.direction = (360 - self.direction) % 360
      self.x = 1

    # if ball hits right side wall
    if self.x > 781:
      self.direction = (360 - self.direction) % 360
      self.x = 780

    # if paddle missed ball
    if self.y > 600:
      return True
    else:
      return False
        

  def draw(self, screen):
    screen.blit(self.image,self.rect)


  def get_x(self):
    return self.x


  def set_x(self, x):
    self.x = x


  def get_y(self):
    return self.y


  def set_y(self, y):
    self.y = y


  def get_collision(self):
    return self.collision


  def set_collision(self, collision):
    self.collision = collision


  def get_rect(self):
    return self.rect


  def set_rect(self, rect):
    self.rect = rect

