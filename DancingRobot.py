from Myro import *
init("sim")
def Sprinkler (y): #Number of spins as the Parameter
    for x in range(0,y):
        turnRight( 3, .5)
        turnLeft( 2, .5)
Sprinkler(30) 
def TwoStep ():
    forward( 3, 1)
    backward( 3, 1)
    turnBy(90)
    forward( 3, 1)
    backward( 3, 2)
    forward( 3, 1)
    turnBy(270)
    forward( 3, 1)
    backward( 3, 1)
    turnBy(90)
    forward( 3, 1)
    backward( 3, 2)
    forward( 3, 1)
    turnBy(270)
TwoStep()
def Spin ():
    forward(2,1)
    turnRight(3,1)
    turnLeft(1,1)
    turnRight(3,1)
    turnRight(2,1)
    forward(2,1)
    turnLeft(3,1)
    turnLeft(2,1)
    turnLeft(4,1)
    turnRight(2,1)
    turnLeft(4,1)
    turnLeft(2,1)
    forward(2,1.5)
    turnRight(3,2)
turnBy(90)
forward(2,1)
Spin ()
Sprinkler()
TwoStep()