from graphics import *
from random import *
class Target:
    def __init__(self,win,xupper,xlower):
        xrange = xupper-xlower
        self.xpos = randrange(0,xrange-9)
        self.ypos = 0
        self.rect = Rectangle(Point(self.xpos-20,0), Point(self.xpos,20))
        self.rect.setFill('red')
        self.rect.draw(win)
        Text(Point(self.xpos - 10, 10), "HIT ME").draw(win)

    def hit(self,shot):
        if shot == 0:
           return False
        elif shot.getY() < 20 and shot.getY() > 0 and shot.getX() < self.xpos and shot.getX() > self.xpos-20:
            return True
        else:
            return False