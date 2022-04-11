from Brick import Brick
from Paddle import Paddle
from Ball import Ball
from Overlay import Overlay
import pygame as pg

# ----------------------------------
# CIS 343 Project 2 - Breakout!
# 
# @author Evan Johns
# @author Andreas Martinez
# @date 4/10/2022
# ----------------------------------

# Sets up the environment, all of the balls, bricks, paddle, etc., and contains the game loop.
class Game:

  screen_width = 800
  screen_height = 600

  def __init__(self):
    # Initialize sound mixer
    pg.init()
    pg.mixer.init()

    # Setup sound effects
    self.background_music = pg.mixer.music.load("./sounds/bgm.mp3")
    self.collision_sound = pg.mixer.Sound("./sounds/col.mp3")

    # Create drawing and display tools
    self.image = pg.Surface((200, 200))
    self.image.fill((0, 101, 103))
    self.react = self.image.get_rect()
    self.screen = pg.display.set_mode((self.screen_width, self.screen_height))
    self.running = True
    self.game_over = False;
    self.clock = pg.time.Clock()
    self.overlay = Overlay()

    # Create paddle and balls
    ball = Ball()
    self.paddle = Paddle()
    self.balls = pg.sprite.Group()  # have to add to group for collision
    self.balls.add(ball)

    # Create bricks
    self.bricks = pg.sprite.Group()
    for row in range(5):
      for colum in range(8):
        brick = Brick(colum * 100, row * 50)
        self.bricks.add(brick)


  def draw(self):
    # Draw all balls, bricks, and the paddle to the display
    self.screen.fill((255, 255, 255))
    self.balls.draw(self.screen)
    self.bricks.draw(self.screen)
    self.paddle.draw(self.screen)
    self.overlay.draw(self.screen)
    pg.display.flip()  # double buffering


  def update(self):
    # Check for collision of each ball in balls
    for ball in self.balls:
      ball.set_collision(False)

      # update ball and check if ball died, spawn new ball
      if ball.update():
        self.overlay.set_lives(self.overlay.get_lives() - 1)
        ball.kill()
        b = Ball()
        self.balls.add(b)
      
      # Check for collision with paddle
      if ball.get_rect().colliderect(self.paddle.get_rect()):
        ball.bounce(0)
        ball.set_collision(True)

      # Check for collision with bricks
      for brick in self.bricks:
        if ball.get_rect().colliderect(brick.get_rect()) and not ball.get_collision():
          # play collision sound effect
          pg.mixer.Sound.play(self.collision_sound)
          # add to the score
          self.overlay.set_score(self.overlay.get_score() + 1)
          # Take health away from brick
          if brick.onHit():
            brick.kill()
          # Bounce the ball
          ball.bounce(0)
          ball.set_collision(True)

  def run(self):
    # Play background music
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.07)

    while self.running:
      # Event Handling
      for event in pg.event.get():
        # If quiting game, end the game
        if event.type == pg.QUIT:
          self.running = False
        # Check for keyboard input
        if event.type == pg.KEYDOWN and not self.game_over:
          if event.key == pg.K_a:
            # Add ball
            self.balls.add(Ball())
          else:
            # Update paddle position
            self.paddle.update(event.key)

      # If out of lives, display end game text
      if self.overlay.get_lives() < 0:
        # end the game
        self.game_over = True
        # remove all the balls
        for ball in self.balls:
          ball.kill()
        # display end screen
        self.overlay.draw(self.screen)
      else:
        # If game is not over, update everything
        self.update()
        self.draw()

      self.clock.tick(60)
    pg.quit()


# Start the game
game = Game()
game.run()
