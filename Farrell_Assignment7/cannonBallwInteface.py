from graphics import *
from projectile import *
from dialog import *
from Target import *
class ShotTracker:

    def __init__(self, win, angle, velocity, height):
        """win is the GraphWin to display the shot, angle, velocity, and
        height are initial projectile parameters.
        """
        self.proj = Projectile(angle, velocity, height)
        self.marker = Circle(Point(0,height), 3)
        self.marker.setFill("red")
        self.marker.setOutline("red")
        self.marker.draw(win)

    def update(self, dt):
        """ Move the shot dt seconds farther along its flight """
        self.proj.update(dt)
        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx,dy)

    def getX(self):
        """ return the current x coordinate of the shot's center """
        return self.proj.getX()
    def getY(self):
        """ return the current y coordinate of the shot's center """
        return self.proj.getY()
    def destroy(self):
        """ undraw the shot """
        self.marker.undraw()


def main():
    # create animation window
    win = GraphWin("Projectile Animation", 640, 480) #, autoflush = False
    win.setCoords(-10, -10, 210, 155)
    # draw baseline
    Line(Point(-10, 0), Point(210, 0)).draw(win)
    # draw labeled ticks every 50 meters
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    angle, vel, height = 60.0, 50, 10.0

    Hit = False

    target = Target(win, 210, -10)

    while True:
        #interact with the user and set first parameters after checking if its been hit already
        if Hit == False:
            inputwin = InputDialog(angle, vel, height)
            choice = inputwin.interact()
            inputwin.close()

            # create a shot and track until it hits ground or leaves window

            angle, vel, height = inputwin.getValues()
            shot = ShotTracker(win, angle, vel, height)

        if choice == "Quit":  # loop exit
            break

        while 0 <= shot.getY() and -10 < shot.getX() <= 210 and Hit == False:
            shot.update(1/50) #1 / 50
            update(50)
            if target.hit(shot) == True:
                Hit = True
                Text(Point(100,80),("Target Hit - Congratulations")).draw(win)
                time.sleep(5)
                win.close()
        shot.destroy()

    win.close()

main()