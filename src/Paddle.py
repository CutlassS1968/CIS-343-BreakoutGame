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

  width = 300
  height =  20

  def __init__(self):
    pg.sprite.Sprite.__init__(self)

    self.image = pg.Surface([self.width, self.height])
    self.image.fill((0, 0, 0))

    self.rect = self.image.get_rect()
    self.rect.x = 150
    self.rect.y = 550


  def draw(self, screen):
    screen.blit(self.image,self.rect)


  def moveLeft(self):
    if self.rect.x - 30 > -1: # so you can move paddle out of screen
        self.rect.x -= 30
    

  def moveRight(self):
    if self.rect.x + 30 < 531: # so you can move paddle out of screen
      self.rect.x += 30
    

  def update(self, key):
    # Move paddle
    if key == pg.K_LEFT:
      self.moveLeft()
    if key == pg.K_RIGHT:
      self.moveRight()


  def get_rect(self):
    return self.rect


  def set_rect(self, rect):
    self.rect = rect

