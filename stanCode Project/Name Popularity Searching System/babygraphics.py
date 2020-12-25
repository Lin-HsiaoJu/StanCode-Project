"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program create the line graph of the name data you search.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    n = len(YEARS)
    x_coordinate = year_index*((width-2*GRAPH_MARGIN_SIZE)/n) + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    # num = The index of the current year in the YEARS list
    num = 0
    for year in YEARS:
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, num)
        num += 1
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # a is the index of the color in the COLORS list.
    a = 0
    for name in lookup_names:
        # num = The index of the current year in the YEARS list
        num = 0
        x_coordinate_list = []
        rank_list = []
        for year in YEARS:
            year = str(year)
            if year in name_data[name]:
                rank_list.append(name_data[name][year])
            else:
                rank_list.append('*')
            x_coordinate_list.append(get_x_coordinate(CANVAS_WIDTH, num))
            num += 1
        y_coordinate_list = []
        for rank in rank_list:
            if rank == '*':
                y_coordinate_list.append(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
            else:
                y_coordinate_list.append((int(rank)/1000)*(CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)+GRAPH_MARGIN_SIZE)
        # i is the index of the x_coordinate in x_coordinate_list
        i = 0
        for x_coordinate in x_coordinate_list:
            c = a % len(COLORS)
            color = COLORS[c]
            canvas.create_text(x_coordinate + TEXT_DX, y_coordinate_list[i], text=name + ' ' + rank_list[i],
                               anchor=tkinter.SW, fill=color)
            if i < len(x_coordinate_list)-1:
                canvas.create_line(x_coordinate, y_coordinate_list[i], x_coordinate_list[i+1],
                                   y_coordinate_list[i+1], width=LINE_WIDTH, fill=color)
            i += 1
        a += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
