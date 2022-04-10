import pygame as pg
from random import randint
from random import seed

# Is a subclass of pygame.sprite.Sprite.
#
# As talked about in class, each subclass of pygame.sprite.Sprite will have a draw() and update() method.
# You will need to override the update() method for anything that moves.
#
# The image will be a randomly chosen color.
#
# You can do this by randomly choosing an int between 0-255 (inclusive) for
# each of the Red, Green, and Blue components.
#
# The health of the brick will be set to 766 - the sum of those values
# (so 0,0,0 or black will have a health of 766 and 255,255,255 will have a health of 1).
#
# Brick should have a hit method that removes 25 from its health and destroys
# itself if health goes to 0 or below.
class Brick(pg.sprite.Sprite):
  def __init__(self, x, y):
    pg.sprite.Sprite.__init__(self)
    # Variables for each brick
    self.red = randint(0,255)
    self.green = randint(0,255)
    self.blue = randint(0,255)
    self.health = self.red+self.green+self.blue
    # making rectangle and color
    self.image = pg.Surface([100,50])
    self.image.fill((self.red, self.green, self.blue))
    #setting the position
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y

  def draw(self, screen):
    screen.blit(self.image,self.rect)

  def onHit(self):
    self.health -= 25

    if self.red - 8 > 0:
      self.red -= 8
    if self.green - 8 > 0:
      self.green -= 8
    if self.blue - 8 > 0:
          self.blue -= 8

    if self.health < 0:
      return True

    #Repaint the new color
    self.image.fill((self.red, self.green, self.blue))

    return False
