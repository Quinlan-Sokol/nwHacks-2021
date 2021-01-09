from graphics import *

# window size [width, height]
wSize = (1500, 1000)

mousePos = Point(0, 0)
windowOpen = True


def createText(win, pos, string, color="black", face="helvetica", size=12, style="normal"):
    t = Text(pos, string)
    t.setFace(face)
    t.setSize(size)
    t.setStyle(style)
    t.setTextColor(color)
    t.draw(win)


def createRectangle(win, p1, p2, fcolor="", ocolor="black", width=1):
    r = Rectangle(p1, p2)
    r.setFill(fcolor)
    r.setOutline(ocolor)
    r.setWidth(width)
    r.draw(win)


def createLine(win, p1, p2, color="black", width=1, arrow="none"):
    l = Line(p1, p2)
    l.setOutline(color)
    l.setWidth(width)
    l.setArrow(arrow)
    l.draw(win)


# clear all items from the window, except for classes within exceptions
def clear(win, exceptions=[]):
    for item in win.items[:]:
        if str(item.__class__.__name__) not in exceptions:
            item.undraw()


# link mouse motion to a variable
def motion(e):
    global mousePos
    mousePos = Point(e.x, e.y)


# callback function for closing the window
def onClose():
    global windowOpen
    windowOpen = False
    window.master.destroy()


# initialize the window
window = GraphWin("Title", wSize[0], wSize[1], autoflush=False)
window.setBackground("black")
window.bind("<Motion>", motion)
window.master.protocol("WM_DELETE_WINDOW", onClose)
window.master.TK_SILENCE_DEPRECATION = 1

while windowOpen:
    clear(window)



    update(10)