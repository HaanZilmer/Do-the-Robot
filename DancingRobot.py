from Myro import *
init("sim")
def Sprinkler ():
    for x in range(0,40):
        turnRight( 3, .5)
        turnLeft( 2, .5)
Sprinkler()
def TwoStep ():
    forward( 3, 1)
    backward( 3, 1)
    turnBy(90)
    forward( 3, 1)
    backward( 6, 2)
    forward( 3, 1)
    turnBy(270)
    forward( 3, 1)
    backward( 3, 1)
    turnBy(90)
    forward( 3, 1)
    backward( 6, 2)
    forward( 3, 1)
    turnBy(270)
TwoStep()
