from graphics import *
from BackgroundCircle import *
from random import randint, choice
from math import sqrt
from pygame import mixer

# window size [width, height]
wSize = (1000, 1000)

mousePos = Point(0, 0)
windowOpen = True

minB = 150
maxB = 255
curB = 150
deltaB = -1

circles = []
circleColors = []
# generate random colors
for k in range(15):
    circleColors.append(color_rgb(30 + randint(-30, 40),
                                  144 + randint(-40, 40),
                                  255 + randint(-40, 0)))


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


def createCircle(win, p, fcolor="", ocolor="black", width=1, radius=1):
    c = Circle(p, radius)
    c.setOutline(ocolor)
    c.setFill(fcolor)
    c.setWidth(width)
    c.draw(win)


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


def distance(p1, p2):
    return sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def drawBackground(win):
    global curB, minB, maxB, deltaB
    color = color_rgb(34, 200, curB)
    createRectangle(win, Point(0, 0), Point(wSize[0], wSize[1]), fcolor=color, ocolor=color)

    if curB == maxB or curB == minB:
        deltaB *= -1
    curB += deltaB


# initialize the window
window = GraphWin("Title", wSize[0], wSize[1], autoflush=False)
window.setBackground("white")
window.bind("<Motion>", motion)
window.master.protocol("WM_DELETE_WINDOW", onClose)
window.master.TK_SILENCE_DEPRECATION = 1

mixer.init()
mixer.music.load("music.wav")
mixer.music.play(loops=-1)

r = 40
for k in range(40):
    pos = Point(randint(r, wSize[0] - r), randint(r, wSize[1] - r))
    while not all(map(lambda c: distance(c.pos, pos) >= r*2, circles)):
        pos = Point(randint(r, wSize[0] - r), randint(r, wSize[1] - r))

    v = Point(randint(-4, 4), randint(-4, 4))
    while v.x == 0 or v.y == 0:
        v = Point(randint(-4, 4), randint(-4, 4))

    circles.append(BackgroundCircle(pos, choice(circleColors), r, v))

while windowOpen:
    clear(window)

    drawBackground(window)

    for c in circles:
        c.update(wSize, circles)
        createCircle(window, c.pos, fcolor=c.color, ocolor="white", radius=c.radius, width=2)

    update(60)
