# 112 Term Project
# Project Cauldron
# Andrew ID: junweih

import math,scipy,numpy,pandas,string,copy,random
from cmu_112_graphics import *
import tkinter as tk

import sys
print(f'sudo "{sys.executable}" -m pip install pillow')
print(f'sudo "{sys.executable}" -m pip install requests')

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


################################################################################
# The Body Part
################################################################################

def playFlappyBird(): 
    runApp(width=700, height=700)

# def realPhysicsEngine(x):
#     g = 9.8
#     timeElapsed = x/g
#     h = timeElapsed*x
#     return h

def appStarted(app):
    app.Bird= [100,app.height/2,0]
    app.timerDelay = 1
    app.r = 33
    app.image1 = app.loadImage('Birdy.gif')
    app.image2 = app.scaleImage(app.image1, 1/9)

def mousePressed(app,event):
    cx = event.x    
    cy = event.y
    app.Bird[2] = -0.25


def timerFired(app):
    currV = app.Bird[2] # the physics engine...
    dis = currV*9.8
    app.Bird[1] += dis
    app.Bird[2] += 0.006


def redrawAll(app,canvas):
    # canvas.create_oval(app.Bird[0]-app.r,
    # app.Bird[1]-app.r,app.Bird[0]+app.r,app.Bird[1]+app.r,fill = 'black') 
    canvas.create_image(app.Bird[0],app.Bird[1],image=ImageTk.PhotoImage(app.image2))























playFlappyBird()
