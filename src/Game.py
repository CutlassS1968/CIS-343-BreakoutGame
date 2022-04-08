import pygame
from random import randint


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
class Ball(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def draw(self):
        print(self)

    def update(self):
        print(self)


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
class Brick(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.width = width
        self.height = height

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def draw(self):
        print(self)


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
class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.height = height
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def draw(self):
        print(self)

    def update(self):
        print(self)


# Draws the score and number of lives.
class Overlay:
    def __init__(self):
        print("Hello, World!")


class Game:
    # Define some colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    blue = (0, 0, 255)

    # Size of break-out blocks
    brick_width = 23
    brick_height = 15

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode([800, 600])
        pygame.display.set_caption('Breakout Game')
        self.font = pygame.font.Font(None, 36)
        self.background = pygame.Surface(self.screen.get_size())

        # Create sprite lists
        self.bricks = pygame.sprite.Group()
        self.balls = pygame.sprite.Group()
        self.allsprites = pygame.sprite.Group()

        self.paddle = Paddle(self.white, 100, 20)
        self.allsprites.add(self.paddle)

        self.ball = Ball(self.white, 10, 10)
        self.allsprites.add(self.ball)
        self.balls.add(self.ball)

        # The top of the block (y position)
        self.top = 80

        # Number of blocks to create
        self.brickcount = 32

        # --- Create blocks

        # Five rows of blocks
        for row in range(5):
            # 32 columns of blocks
            for column in range(0, self.brickcount):
                # Create a block
                color = pygame.color.Color(randint(0, 255),
                                           randint(0, 255),
                                           randint(0, 255))
                brick = Brick(color, column * (self.brick_width + 2) + 1, self.top)
                self.bricks.add(brick)
                self.allsprites.add(brick)
            # Move the top of the next row down
            self.top += self.brick_height + 2

        # limit the speed (don't need to be going super fast)
        self.clock = pygame.time.Clock()

        # exit loop condition
        self.game_over = False

        # end game condition
        self.exit_program = False

    def run(self):
        # Main program loop
        while not self.exit_program:
         
            # Limit to 30 fps
            self.clock.tick(30)
         
            # Clear the screen
            self.screen.fill(self.black)
         
            # Process the events in the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_program = True
         
            # Draw Everything
            self.allsprites.draw(self.screen)
         
            # Flip the screen and show what we've drawn
            pygame.display.flip()
         
        pygame.quit()


g = Game()
g.run()
