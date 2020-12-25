"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

This program create breakout game which give you three opportunities to try.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    # Add animation loop here!
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

    while True:
        pause(FRAME_RATE)
        if lives > 0:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            obj = graphics.test()
            graphics.check(obj)
            graphics.ball.move(dx, dy)
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width > graphics.window.width:
                graphics.bouncing_x()
            if graphics.ball.y <= 0:
                graphics.bouncing_y()
            if graphics.ball.y + graphics.ball.height > graphics.window.height:
                lives -= 1
                graphics.turn = True
                graphics.put_the_ball_position()
                graphics.reset_speed()

        else:
            graphics.fail()
            break












if __name__ == '__main__':
    main()
