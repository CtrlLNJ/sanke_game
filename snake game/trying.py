from graphics import *
def interface():
    win = GraphWin()
    win.setCoords(0,0,10,10)
    p = Polygon(Point(7,7.5),Point(7,5.5),Point(2,5.5),Point(2,7.5))
    p.setFill("white")
    p.draw(win)
    t1 = Text(Point(4.5,7),"Start Snake Game?")
    t2 = Text(Point(3.5,6),"Yes")
    t3 = Text(Point(5,6),"Cancel")
    t1.draw(win)
    t2.draw(win)
    t3.draw(win)
    if win.getMouse() == t3:
        win.close()
    elif win.getMouse() == t2:
        t1.undraw()
        t2.undraw()
        t3.undraw()
    else:
        t1.undraw()
        t2.undraw()
        t3.undraw()

interface()

def getMouse(self):
    """Wait for mouse click and return Point object representing
    the click"""
    self.update()      # flush any prior clicks
    self.mouseX = None
    self.mouseY = None
    while self.mouseX == None or self.mouseY == None:
        self.update()
        if self.isClosed(): raise GraphicsError("getMouse in closed window")
        time.sleep(.1) # give up thread
    x,y = self.toWorld(self.mouseX, self.mouseY)
    self.mouseX = None
    self.mouseY = None
    return Point(x,y) # How to print the number of this point and how to use it into the programming
