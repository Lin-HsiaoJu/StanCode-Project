"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

The class will provide the structure of the breakout game.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        self.ball_radius = ball_radius
        self.paddle_offset = paddle_offset
        self.brick_width = brick_width
        self.brick_height = brick_height
        self.brick_spacing = brick_spacing
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.brick_offset = brick_offset
        # the amount of the bricks removed
        self.amount = 0
        # the total amount of bricks in the game
        self.total = self.brick_rows * self.brick_cols

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.set_the_paddle_position()
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.put_the_ball_position()
        self.window.add(self.ball)

        self.__dx = 0
        self.__dy = 0
        self.turn = True
        # Default initial velocity for the ball.
        onmouseclicked(self.start)

        # Initialize our mouse listeners.
        onmousemoved(self.paddle_move)

        # Draw bricks.

        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(self.brick_width, self.brick_height)
                self.brick.x = 0+j*(self.brick_width+self.brick_spacing)
                self.brick.y = self.brick_offset+i*(self.brick_height+self.brick_spacing)
                self.brick.filled = True
                self.brick.color = 'white'
                if i % 14 == 0 or i % 14 == 1:
                    self.brick.fill_color = 'red'
                if i % 14 == 2 or i % 14 == 3:
                    self.brick.fill_color = 'orange'
                if i % 14 == 4 or i % 14 == 5:
                    self.brick.fill_color = 'yellow'
                if i % 14 == 6 or i % 14 == 7:
                    self.brick.fill_color = 'green'
                if i % 14 == 8 or i % 14 == 9:
                    self.brick.fill_color = 'blue'
                if i % 14 == 10 or i % 14 == 11:
                    self.brick.fill_color = 'magenta'
                if i % 14 == 12 or i % 14 == 13:
                    self.brick.fill_color = 'purple'
                self.window.add(self.brick, self.brick.x, self.brick.y)

    # if mouse click,the game will be start
    def start(self, mouse):
        if self.turn is True:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -1 * self.__dx
            self.turn = False

    # put __dx to breakout.py
    def get_dx(self):
        return self.__dx

    # put __dy to breakout.py
    def get_dy(self):
        return self.__dy

    # make the paddle can follow the mouse route and will not out of window
    def paddle_move(self, mouse):
        if 0 <= mouse.x <= self.window.width-self.paddle.width:
            self.paddle.x = mouse.x
            self.paddle.y = self.window.height-self.paddle.height-self.paddle_offset
        if mouse.x <= 0:
            self.paddle.x = 0
            self.paddle.y = self.window.height-self.paddle.height-self.paddle_offset
        if self.window.width-self.paddle.width <= mouse.x:
            self.paddle.x = self.window.width-self.paddle.width
            self.paddle.y = self.window.height-self.paddle.height-self.paddle_offset

    # set the starting point of paddle
    def set_the_paddle_position(self):
        self.paddle.x = (self.window.width-self.paddle.width)/2
        self.paddle.y = (self.window.height-self.paddle.height-self.paddle_offset)

    # set the starting point of ball
    def put_the_ball_position(self):
        self.ball.x = (self.window.width - self.ball_radius) / 2
        self.ball.y = (self.window.height - self.ball_radius) / 2

    # check if the ball touched any object
    def test(self):
        something = self.window.get_object_at(self.ball.x, self.ball.y)
        if something is not None:
            return something
        something = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        if something is not None:
            return something
        something = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        if something is not None:
            return something
        something = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)
        if something is not None:
            return something

    # if the ball touched object which is paddle or brick will be removed.
    def check(self, a):
        if a is self.paddle and self.__dy > 0:
            self.__dy *= -1
        if a is not self.paddle:
            if a is not None:
                if self.__dy < 0:
                    self.window.remove(a)
                    self.amount += 1
                    if self.amount == self.total:
                        self.reset_speed()
                    self.__dy *= -1

    # make the ball stop
    def reset_speed(self):
        self.__dx = 0
        self.__dy = 0

    # if the ball touched the window or object, the ball will be bounced
    def bouncing_x(self):
        self.__dx *= -1

    # if the ball touched the window or object, the ball will be bounced
    def bouncing_y(self):
        self.__dy *= -1

    # if the player lose for three times, the game will shut down
    def fail(self):
        lose = GLabel('YOU FAILED')
        lose.font = '-80'
        lose.color = 'grey'
        self.window.add(lose, (self.window.width - lose.width) / 2, self.window.height)











