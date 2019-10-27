###############################################################################
# Wrapper for the graphcis library available at
# http://mcsp.wartburg.edu/zelle/python/ modified (in a quite hideous manner
# in order to remove the requirement to understand Object Orientation)
#
# Author: Joel Fergusson joel.fergusson@york.ac.uk
#
# A note on colours:
# Colours are represented as strings. You can use colour names, e.g. "black",
# "magenta", or you can use the getRGBColour function. Usage example:
# setBackgroundColour("red")
# or
# setBackgroundColour(getRGBColour(255, 0, 0))
#
###############################################################################

import graphics

# Unfortunately, globals are a requirement for removing the Object orientation
# Begin with underscore to not intefere with students code.
global _window
global _current_point
global _objects
global _current_line_thickness
global _current_line_colour
global _current_fill_colour
global _clear_canvas
_objects = []
_current_line_thickness = 1
_current_line_colour = "black"
_current_fill_colour = "black"
_text_properties = {"size": 10, "face": "helvetica", "style": "normal", "align": "left", "anchor": "center"}
_clear_canvas = False


def openWindow(width=400, height=400, title="Snake Game"):
    """ Opens a window of specified size, with specified title.
    Default 800x600 pixels, title "Graphics Window".

    @param width Width of the window in pixels
    @param height Height of the window in pixels
    @param title Title of the window (String)
    """
    global _window
    global _current_point

    # Open the window
    _window = graphics.GraphWin(title, width, height)

    # Set a current point to start drawing from as (0, 0)
    _current_point = graphics.Point(0, 0)


def closeWindow():
    """Closes graphics window
    """
    _window.close()


def updateCanvas():
    """Updates the canvas. I.E. draws all the objects onto the canvas
    that have been added since the last update or clear. 
    """
    global _clear_canvas
    if _clear_canvas:
        for i in _window.items[:]:
            i.undraw()
        del _window.items[:]
        _window.items = []
        del _objects[:_clear_canvas]
    _clear_canvas = False

    # Draw all objects that belong on the canvas in the order they were added
    for i in _objects:
        try:
            i.draw(_window)
        except graphics.GraphicsError as e:
            # Catch error where object is already drawn - this is okay.
            pass


def clearCanvas():
    """Clears the canvas to background colour.
    """
    global _clear_canvas
    global _objects
    _clear_canvas = len(_objects)


def setCanvasColour(colour):
    """Sets the background colour of the canvas to the specified colour
    """
    _window.setBackground(colour)


def moveTo(x, y):
    """Moves the graphics pen to specified cooordinate
    @param x X coordinate to move graphics pen to
    @param y Y coordinate to move graphics pen to
    """
    _current_point.x = x
    _current_point.y = y


def drawLine(x, y):
    """Draws a line from the current graphics pen point given
    by vector (x, y). Moves the graphics pen point
    @param x Length of line in X direction
    @param y Length of line in Y direction
    """
    # For some silly reason, the line takes its fill colour
    shape = graphics.Line(_current_point,
                          graphics.Point(_current_point.x + x, _current_point.y + y))
    shape.setFill(_current_line_colour)
    shape.setWidth(_current_line_thickness)
    _objects.append(shape)
    moveTo(_current_point.x + x, _current_point.y + y)


def drawImage(filename):
    """Draws an image given by filename (should be in the same folder as your
    python script). The top left of the image is the current graphics pen point.
    @param filename Filename of image to display. Must be a gif.
    """
    im = graphics.Image(_current_point, [filename])
    im.config["anchor"] = "nw"
    _objects.append(im)


def drawText(text):
    """Draws text anchored at graphics pen point. The colour is given by the
    current line colour, and the properties of the text can be changed by
    setTextProperties().
    @param text String to write to screen
    """
    text = graphics.Text(_current_point, text)
    text.setFace(_text_properties["face"])
    text.setSize(_text_properties["size"])
    text.setStyle(_text_properties["style"])
    text.setTextColor(_current_line_colour)
    # Hack into the graphics library to set both justification and anchor point
    text.config["justify"] = _text_properties["align"]
    text.config["anchor"] = _text_properties["anchor"]
    _objects.append(text)


def setTextProperties(face=None, size=None, style=None, align=None, anchor=None):
    """Sets the properties of the next text objects to write.
    @param face Face (font) of the text. Legal values: "helvetica", "arial",
    "courier", "times roman". Passing None will not change the current font.
    @param size Size of the text, numberical, range 5-36. Passing None will leave this
    alone
    @param style Style of the text. Legal values: "bold","normal","italic",
    "bold italic". Passing None will not change the current style.
    @param align Alignment of text from anchor point. Legal values:
    "centre", "left", right".
    @param anchor Anchor location. Defines where the text is drawn relative to the
    graphics pen point. Legal values: "n", "ne", "e", "se", "s", "sw", "w", "nw", or
    "centre"
    """
    if face != None:
        _text_properties["face"] = face
    if size != None:
        _text_properties["size"] = size
    if style != None:
        _text_properties["style"] = style

    if align != None:
        # Align requires manual processing since it's an extension on the
        # graphics library in use.
        if align in ["centre", "left", "right"]:
            # Americanize
            if align == "centre":
                align = "center"
            _text_properties["align"] = align
        else:
            raise graphics.GraphicsError("Invalid align string")

    if anchor != None:
        # Anchor requires manual processing since it's an extension on the
        # graphics library in use.
        if anchor in ["n", "ne", "e", "se", "s", "sw", "w", "nw", "centre"]:
            # Americanize
            if anchor == "centre":
                anchor = "center"
            _text_properties["anchor"] = anchor
        else:
            raise graphics.GraphicsError("Invalid anchor string")


def setLineColour(colour):
    """Sets the line colour of any subsequent objects to be drawn
    @param colour Colour to use, see note in file
    """
    global _current_line_colour
    _current_line_colour = colour


def setLineThickness(thickness):
    """Sets the line thickness of any subsequent objects to be drawn
    @param thickness Thickness of lines in pixels
    """
    global _current_line_thickness
    _current_line_thickness = thickness


def waitForKeyPress():
    """Waits for a key press and returns press as string.

    @return the key pressed
    """
    return _window.getKey()


def getKeyPress():
    """Waits for a key press and returns press as string.

    @return the key pressed
    """
    return _window.checkKey()


def waitForMouseClick():
    """Waits for a mouse click and returns the coordinates of
    the click as a tuple.

    @return (x, y) x and y coordinates of mouse click.
    """
    # Call graphics library and return coordinates of click as tuple
    mouse_point = _window.getMouse()
    return (mouse_point.x, mouse_point.y)


def getRGBColour(r, g, b):
    """Returns a string that represents any RGB colour
    @param r Red component of colour (0-255)
    @param g Green component of colour (0-255)
    @param b Blue component of colour (0-255)
    @return colour to use in functions
    """
    return graphics.color_rgb(r, g, b)
