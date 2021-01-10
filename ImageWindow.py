from graphics import *
from tkinter.filedialog import asksaveasfile


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


# determines if Point p is within a rectangle
def inRect(p, r1, r2):
    return r1.x <= p.x <= r2.x and r1.y <= p.y <= r2.y


class ImageWindow:

    def __init__(self, im, n):
        self.image = im
        self.name = n
        self.isAlive = True
        self.window = GraphWin("Enjoy!", im.size[0], im.size[1], autoflush=True)
        self.window.master.TK_SILENCE_DEPRECATION = 1
        self.window.master.overrideredirect(True)

        self.drawImage = Image(Point(im.size[0]/2, im.size[1]/2), "assets/Temp Images/" + n)
        self.drawImage.draw(self.window)

        createRectangle(self.window, Point(10, im.size[1] - 10 - 40), Point(10 + 120, im.size[1] - 10), fcolor="black", ocolor=color_rgb(57, 255, 20), width=2)
        createText(self.window, Point(70, im.size[1] - 30), "Download", color="white", size=16, style="bold")

        createRectangle(self.window, Point(im.size[0] - 10 - 120, im.size[1] - 10 - 40), Point(im.size[0] - 10, im.size[1] - 10), fcolor="black", ocolor=color_rgb(57, 255, 20), width=2)
        createText(self.window, Point(im.size[0] - 70, im.size[1] - 30), "Cancel", color="white", size=16, style="bold")

    def update(self):
        #check for clicks
        click = self.window.checkMouse()
        if click is not None:
            if inRect(click, Point(10, self.image.size[1] - 10 - 40), Point(10 + 120, self.image.size[1] - 10)):
                path = asksaveasfile(mode="wb", defaultextension=".png")
                if path is not None:
                    print(path)
                    self.image.save(path)
            if inRect(click, Point(self.image.size[0] - 10 - 120, self.image.size[1] - 10 - 40), Point(self.image.size[0] - 10, self.image.size[1] - 10)):
                self.isAlive = False
                self.window.master.destroy()
