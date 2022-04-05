import pygame


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
class Ball(pygame.sprite.Sprite()):
    def __init__(self):
        print("Hello, World!")

    def draw(self):
        print(self)

    def update(self):
        print(self)

