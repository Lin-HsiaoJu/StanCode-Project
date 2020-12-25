"""
File: best_photoshop_award.py
Name: Jeffrey.Lin 2020/08
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

# Controls the threshold of detecting green screen pixel
THRESHOLD = 1.3
# Controls the upper bound for black pixel
BLACK_PIXEL = 120


def main():
    """
    This function conducts green screen replacement
    that is able to photoshop myself onto a cool background.
    """
    fg = SimpleImage('image_contest/jeffrey.jpg')
    bg = SimpleImage('image_contest/bg.jpg')
    fg.show()
    bg.show()
    bg.make_as_big_as(fg)
    combined_img = combine(bg, fg)
    combined_img.show()


def combine(bg, fg):
    """
    : param1 bg: SimpleImage, the background image
    : param2 fg: SimpleImage, green screen figure image
    : return fg: SimpleImage, the green screen pixels are replaced by pixels background image
    """
    for y in range(fg.height):
        for x in range(fg.width):
            pixel_fg = fg.get_pixel(x, y)
            avg = (pixel_fg.red + pixel_fg.blue + pixel_fg.green) // 3
            total = pixel_fg.red + pixel_fg.blue + pixel_fg.green
            if pixel_fg.green > avg*THRESHOLD and total > BLACK_PIXEL:
                pixel_bg = bg.get_pixel(x, y)
                pixel_fg.green = pixel_bg.green
                pixel_fg.red = pixel_bg.red
                pixel_fg.blue = pixel_bg.blue
    return fg


if __name__ == '__main__':
    main()
