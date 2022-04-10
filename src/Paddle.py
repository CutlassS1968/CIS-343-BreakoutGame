import pygame as pg


# Is subclass of pygame.sprite.Sprite.
#
# As talked about in class, each subclass of pygame.sprite.Sprite will have a draw() and update() method.
# You will need to override the update() method for anything that moves.
#
# The image will just be a black rectangle.
#
# The class should hold information about the size and movement speed of the rectangle
# that represents the paddle.
#
# There should be methods to move the paddle left and right
# at that speed.
#
# Movement should be capped so the paddle can't move off the screen.
class Paddle(pg.sprite.Sprite):
  def __init__(self):
    pg.sprite.Sprite.__init__(self)

    self.image = pg.Surface([100, 20])
    self.image.fill((255,255,255))

    self.rect = self.image.get_rect()
    self.rect.x = 350
    self.rect.y = 500

  def draw(self, screen):
    screen.blit(self.image,self.rect)

  def moveLeft(self):
    self.rect.x -= 10
    
  def moveRight(self):
    self.rect.x += 10
    
  #def update(self):


