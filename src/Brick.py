import pygame


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
class Brick(pygame.sprite.Sprite()):
    def __init__(self):
        print("Hello, World!")

    def draw(self):
        print(self)

