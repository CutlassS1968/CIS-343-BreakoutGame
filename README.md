# CIS-343-BreakoutGame



For this assignment, you will create a game in Python.  We will use the PyGame library; for those of you who are not familiar with it - don't worry!  We will go over the basics in class.


Specifically, we will be making the game Breakout.  You may have played something similar:

![example](https://github.com/CutlassS1968/CIS-343-BreakoutGame/blob/main/resources/example.png)


The colored bricks at the top must be broken by the ball(s). The paddle keeps the ball in play.

This game must be Object-Oriented.  You must have the following classes:


- Game - Sets up the environment, all of the balls, bricks, paddle, etc., and contains the game loop.

- Overlay - Draws the score and number of lives.

- Paddle - Is subclass of pygame.sprite.Sprite.  The image will just be a black rectangle.  The class should hold information about the size and movement speed of the rectangle that represents the paddle.  There should be methods to move the paddle left and right at that speed.  Movement should be capped so the paddle can't move off the screen.

- Ball - Is a subclass of pygame.sprite.Sprite.  The image will be a circle.  The balls will bounce off walls, the paddle, and bricks.  When a ball bounces off a brick, the brick will receive damage if 25.

- Brick - Is a subclass of pygame.sprite.Sprite.  The image will be a randomly chosen color.  You can do this by randomly choosing an int between 0-255 (inclusive) for each of the Red, Green, and Blue components.  The health of the brick will be set to 766 - the sum of those values (so 0,0,0 or black will have a health of 766 and 255,255,255 will have a health of 1).  Brick should have a hit method that removes 25 from its health and destroys itself if health goes to 0 or below.


As talked about in class, each subclass of pygame.sprite.Sprite will have a draw() and update() method.  You will need to override the update() method for anything that moves.


Grading


Code is commented according to the CIS Style Guide https://www.cis.gvsu.edu/java-coding-style-guide/ - 10 points

Code is object oriented and instance variables are marked private (double underscore before the name) - 10 points

Code uses encapsulation (always uses getters/setters for private data) - 10 points

Python3 (not Python2!) - 10 points

Hidden keystroke that adds an additional ball when pressed - 10 points

Paddle works and coded correctly - 10 points

Balls work and coded correctly - 10 points

Bricks work and coded correctly - 10 points

Uses built-in collision detection methods - 10 points

Adds background music and sounds - 10 points


Total 100 points.


"coded correctly" means adheres to OO ideas we talked about in class, limited code duplication, full use of encapsulation, and polymorphism where approrpriate.


Due date:


April 10 8:00 a.m.
