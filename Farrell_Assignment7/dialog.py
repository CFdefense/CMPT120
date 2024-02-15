"""dialog.py
Provides two classes to work with interfaces Button and InputDialog"""

from graphics import *

class Button:
    """A button is a labeled rectangle in a window .
    It is activated or deactivated with the activate ()
    and deactivate () methods . The clicked (p) method
    returns true if the button is active and p is inside it ."""
    def __init__(self , win , center , width , height , label):
        """ Creates a rectangular button , eg:
        qb = Button (myWin , centerPoint , width , height , 'Quit') """
        w , h = width/2.0 , height/2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"

        return (self.active and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

class InputDialog:
    """A custom window for getting simulation values (angle, velocity,
and height) from the user."""
    def __init__(self, angle, vel, height):
        """ Build and display the input window"""
        self.win = win = GraphWin("Initial Values", 200, 300)
        win.setCoords(0,4.5,4,.5)
        Text(Point(1,1), "Angle").draw(win)
        self.angle = Entry(Point(3,1), 5).draw(win)
        self.angle.setText(str(angle))
        Text(Point(1,2), "Velocity").draw(win)
        self.vel = Entry(Point(3,2), 5).draw(win)

        self.vel.setText(str(vel))
        Text(Point(1,3), "Height").draw(win)
        self.height = Entry(Point(3,3), 5).draw(win)
        self.height.setText(str(height))
        self.fire = Button(win, Point(1,4), 1.25, .5, "Fire ! ")
        self.fire.activate()
        self.quit = Button(win, Point(3,4), 1.25, .5, "Quit")
        self.quit.activate()

    def interact(self):
        """ wait for user to click Quit or Fire button
        Returns a string indicating which button was clicked
        """
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire ! "

    def getValues(self):
        """ return input values """
        a = float (self.angle.getText())
        v = float (self.vel.getText())
        h = float (self.height.getText())
        return a,v,h
    def close (self):
        """close the input window"""
        self.win.close()