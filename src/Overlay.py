import pygame as pg


# Draws the score and number of lives.
class Overlay:
  
    def __init__(self):
      # Initialize font
      pg.init()

      # Set overlay variables
      self.lives = 3
      self.score = 0
      self.font = pg.font.Font('freesansbold.ttf', 32)


    def draw(self, screen):
      if self.lives > 0:
        # Show lives and score
        img = self.font.render('Lives: %s Score: %s' % (self.lives, self.score), True, (0, 0, 0))
        screen.blit(img,  (20, 20))
      else:
        # Show end screen text
        img = self.font.render('Game Over!', True, (0, 0, 0))
        screen.blit(img, (300, 400))


    def get_lives(self):
      return self.lives


    def set_lives(self, lives):
      if lives < 0:
        return False
      self.lives = lives


    def get_score(self):
      return self.score


    def set_score(self, score):
      self.score = score
