import pygame as pg
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
  speed = 2
  x = 400
  y = 500

  direction = 0

  def __init__(self):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.Surface([20, 20])
    self.image.fill((255,255,255))
    self.rect = self.image.get_rect()

  def bounce(self, diff):
    self.direction = (180 - self.direction) % 360
    self.direction -= diff

  def update(self):
    dir_radians = math.radians(self.direction)

    self.x += self.speed * math.sin(dir_radians)
    self.y -= self.speed * math.cos(dir_radians)

    self.rect.x = self.x
    self.rect.y = self.y

    if self.y <= 0:
      self.bounce(0)
      self.y = 1

    if self.x <= 0:
      self.direction = (360 - self.direction) % 360
      self.x = 1

    if self.x > 781:
      self.direction = (360 - self.direction) % 360
      self.x = 780
        
  def draw(self, screen):
    screen.blit(self.image,self.rect)


