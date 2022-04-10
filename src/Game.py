from Brick import Brick
from Paddle import Paddle
import pygame as pg


# Sets up the environment, all of the balls, bricks, paddle, etc., and contains the game loop.
class Game:
  def __init__(self):
    pg.sprite.Sprite.__init__(self)
    self.image = pg.Surface((200,200))
    self.image.fill((0, 101, 103))
    self.react = self.image.get_rect()
	
  def draw(self, screen):
    screen.blit(self.image,self.rect)

  screen = pg.display.set_mode((800,600))
  running = True
  clock = pg.time.Clock()

  
  paddle = Paddle()
  bricks = pg.sprite.Group()


  for row in range(5):
    for colum in range(8):
      brick = Brick(colum * 100, row*50)
      bricks.add(brick)

  brick = Brick(500, 500)
  while running:
    # Event Handling
    for event in pg.event.get():
      if event.type == pg.QUIT:
        running = false

      # Collision for ball & brick
      if event.type == pg.MOUSEBUTTONDOWN:
        # THIS WHOLE SPRITE 4 IS JUST TO PRETEND TO BE THE BALL BUT ITS YOUR MOUSE
        x, y = pg.mouse.get_pos()
        sprite4 = pg.sprite.Sprite()
        sprite4.image = pg.Surface([3, 3])
        sprite4.image.fill((30, 30, 30))
        sprite4.rect = sprite4.image.get_rect()
        sprite4.rect.x = x
        sprite4.rect.y = y
        for brick in bricks:
          # HERE YOU WOULD PULL BALL.RECT
          if sprite4.rect.colliderect(brick.rect):
            deleteBrick = brick.onHit()
            if deleteBrick:
              brick.kill()
      if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
          paddle.moveLeft()
        if event.key == pg.K_RIGHT:
          paddle.moveRight()


    #Object Updating

    # Redrawing
    screen.fill((0,0,0))
    bricks.draw(screen)
    brick.draw(screen)
    paddle.draw(screen)
    pg.display.flip() # double buffering
    clock.tick(60)
  pg.quit()
