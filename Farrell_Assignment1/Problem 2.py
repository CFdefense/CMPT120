#Distance Formula
#program that allows the user to input the X and Y coordinates of two
#points in the plane and calculate their distance.
import math
def DistanceFormula():
    #Welcome Message
    print("This program will calculate the distance between two points")


    numberOfprints = int(input("How many pairs of points would you like to calculate the distance for?"))


    #Inputs loop depening on how many points they are calculating

    for x in range(numberOfprints):
        x1, y1 = eval(input("Please enter the coordinates of the First point (seperated by a comma)"))
        x2, y2 = eval(input("Please enter the coordinates of the Second point (seperated by a comma)"))

        #Equation for Distance
        distance = math.sqrt(((x1-x2)**2)+((y2-y1)**2))


        print("The Distance Between (", x1 ,",", y1 ,") and (", x2 ,",", y2 ,") is " , distance)
DistanceFormula()