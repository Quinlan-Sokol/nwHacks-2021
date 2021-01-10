from graphics import *


class ImageWindow:

    def __init__(self, im, n):
        self.image = im
        self.name = n
        self.window = GraphWin("Enjoy!", im.size[0], im.size[1], autoflush=True)
        self.window.master.TK_SILENCE_DEPRECATION = 1

        self.drawImage = Image(Point(im.size[0]/2, im.size[1]/2), "Temp Images/" + n)
        self.drawImage.draw(self.window)

    def update(self):
        pass
