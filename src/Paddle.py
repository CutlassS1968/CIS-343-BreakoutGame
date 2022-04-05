import pygame


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
class Paddle(pygame.sprite.Sprite()):
    def __init__(self):
        print("Hello, World!")

    def draw(self):
        print(self)

    def update(self):
        print(self)

