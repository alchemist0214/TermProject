###################                                         ###################
##                           ALIEN : TERM PROJECT                            ##
###################                                         ###################
from cmu_112_graphics import *
import math,pandas,numpy,scipy,copy,string,random
import tkinter as tk
#########################################
# version 1
## SOME 2-D surivival game REMASTERED ##

# Let's call it, I don't know, how about Alien: Term Project

################# initialization ###############

class person(object):
    def __init__(self,numba):
        self.number = numba
        if self.number  == 1: #  engineer
            self.speed = 7
            self.attack = 23
            self.hp = 50
            self.ammo = 50
        elif self.number  == 2 : # mercenary 
            self.speed = 6
            self.attack = 27
            self.hp = 40
            self.ammo = 50
        elif self.number  == 3 : # sniper
            self.speed = 9
            self.attack = 45
            self.hp = 20
            self.ammo = 50
        elif self.number  == 4 : #  juggernaut
            self.speed = 4
            self.attack = 6
            self.hp = 60
            self.ammo = 50
        elif self.number  == 4 : #  general
            self.speed = 7
            self.attack = 29
            self.hp = 35
            self.ammo = 50
        elif self.number  == 6 : # the great spartan, 117, Master Chief 
            self.speed = 12
            self.attack = 70
            self.hp = 160
            self.ammo = 50

class enemy(person):
    def __init__(self,number,x,y):
        self.coord = (x,y)
        if number == 7: # regular enemy
            self.number = 7
            self.speed = 20
            self.attack = 3
            self.hp = 50
        if number == 7: # heavy enemy
            self.number = 8
            self.speed = 4
            self.attack = 6
            self.hp = 100
        if number == 8: # boss
            self.number = 8
            self.speed = 7
            self.attack = 21
            self.hp = 80


def appStarted(app):
    app.mode = 'play'
    app.pointer = 1
    RabbitImage = app.loadImage('rabbit.jpg')
    app.Rabbit = []
    for i in range(4):
        sprite = RabbitImage.crop((4+119*i,5,121+123*i,192))
        app.Rabbit.append(sprite)
    app.rabbitCounter = 0
    app.pointer = 0
    app.background  = app.loadImage('be.jpg')
    app.background2 = app.scaleImage(app.background, 1.5)
    app.player1 = person(1)
    app.p1coord = [app.width/2,app.height/2]
    app.player2 = person(2)
    app.p2coord = [app.width/2,app.height/2]
    app.timerCount = 50000
    app.gunfire = [(1,1),(1,1)]
    app.enemyList = []


################# the menu screen ###############

def menu_timerFired(app):
    app.rabbitCounter = (1+app.rabbitCounter)%len(app.Rabbit)              

def menu_keyPressed(app,event):
    if event.key == "Down":
        app.pointer += 1
    if event.key == 'Up':
        app.pointer -= 1
    if event.key == 'F':
        app.mode = 'prePlay'

def menu_redrawAll(app,canvas):
    woo = app.Rabbit[app.rabbitCounter]
    canvas.create_image(app.width/2,app.height/2,image = ImageTk.PhotoImage(app.background2))
    #canvas.create_image(app.width/2,app.height/2,image = ImageTk.PhotoImage(woo))
    canvas.create_text(app.width/2,app.height/4,text = 'Press F to play', font = 'impact 40 bold')

################# the prePlay mode ###################

def prePlay_mousePressed(app, event):
    x,y =  event.x,event.y
    if 0<x and x< app.width/4:
        app.player1 = person(1)
        app.mode = 'preprePlay'
    elif app.width/4<x and x< 2*(app.width/4):
        app.player1 = person(2)
        app.mode = 'preprePlay'
    elif 2*(app.width/4)< x and x<3*(app.width/4):
        app.player1 = person(3)
        app.mode = 'preprePlay'
    elif 3*(app.width/4)<x and x< app.width:
        app.player1 = person(4)
        app.mode = 'preprePlay'
    
def prePlay_redrawAll(app, canvas):
    canvas.create_image(app.width/2,app.height/2,image = ImageTk.PhotoImage(app.background ))
    canvas.create_text(app.width/2,  30,
                       text='Choose Character 1', font='impact 30 bold')

################# the preprePlay mode ###################

def prePlay_mousePressed(app, event): # choose player 2.
    x,y =  event.x,event.y
    if 0<x and x< app.width/4:
        app.player1 = person(1)
        app.mode = 'terrain'
    elif app.width/4<x and x< 2*(app.width/4):
        app.player1 = person(2)
        app.mode = 'terrain'
    elif 2*(app.width/4)< x and x<3*(app.width/4):
        app.player1 = person(3)
        app.mode = 'terrain'
    elif 3*(app.width/4)<x and x< app.width:
        app.player1 = person(4)
        app.mode = 'terrain'
    
def prePlay_redrawAll(app, canvas):
    canvas.create_image(app.width/2,app.height/2,image = ImageTk.PhotoImage(app.background ))
    canvas.create_text(app.width/2,  30,
                       text='Choose Character 2', font='impact 30 bold')

################ choose Terrain ##################

def terrain_mousePressed(app,event): # under construction.
    x = event.x
    y = event.y
    app.mode = 'play'

############### play mode ##############################

def play_timerFired(app):
    app.timerCount -= 1
    if (app.timerCount)%3 == 0:
        n = random.randint(7,8) # we would surely add more enemy types 
        x = random.randint(0,app.width)
        y = random.randint(0,app.height)
        newEnemy = enemy(n,x,y)
        app.enemyList.append(newEnemy)
    


def play_keyPressed(app,event): # I legit don't want to have this slow, glithcy console control. That's it. I will use pygame unless smth comes up.
    # the control console of player 1
    if event.key == 'W' :
        app.p1coord[1] -= app.player1.speed 
    if event.key == 'S':
        app.p1coord[1] += app.player1.speed
    if event.key == 'A':
        app.p1coord[0] -= app.player1.speed 
    if event.key == 'D':
        app.p1coord[0] += app.player1.speed

    ###############################
    if event.key == 'W' and 'A' :
        app.p1coord[1] -= app.player1.speed 
        app.p1coord[0] -= app.player1.speed 
    if event.key == 'W' and 'D':
        app.p1coord[1] -= app.player1.speed
        app.p1coord[0] += app.player1.speed
    if event.key == 'S' and 'A' :
        app.p1coord[1] -= app.player1.speed
        app.p1coord[0] -= app.player1.speed  
    if event.key == 'S' and 'D':
        app.p1coord[1] -= app.player1.speed
        app.p1coord[0] += app.player1.speed


    
    
    # # the control console of player 2
    # if event.key == 'Up':
    #     app.p1coord[0] += app.player1.speed 
    # if event.key == 'Down':
    #     app.p1coord[0] -= app.player1.speed
    # if event.key == 'Left':
    #     app.p1coord[1] -= app.player1.speed 
    # if event.key == 'Right':
    #     app.p1coord[1] += app.player1.speed

def IsHit(x1,y1,x2,y2,x3,y3):
    
    if (x3-x2)/(y3-y2) == (x2-x1)/(y2-y1):
        return True
    else:
        return False # This function would be rewrittern in TP 1 or 2, because we would add obstacle

def play_mousePressed(app,event):
    x = event.x
    y = event.y
    cx = app.p1coord[0]
    cy = app.p1coord[1]
    app.gunfire[0] = (cx,cy)
    app.gunfire[1] =  (x,y)
    for enemy in app.enemyList:
        if IsHit(x,y,cx,cy,enemy.coord[0],enemy.coord[1]):
            enemy.hp -= app.player1.attack
            if enemy.hp <= 0:
                enemy.coord[0],enemy.coord[1] = 10,10

def play_redrawAll(app,canvas):
    canvas.create_oval(app.p1coord[0]+10,app.p1coord[1]+10,app.p1coord[0]-10,app.p1coord[1]-10,fill = 'black')
    for enemy in app.enemyList:
        canvas.create_oval(enemy.coord[0]+10,enemy.coord[1]+10,enemy.coord[0]-10,enemy.coord[1]-10,fill = 'red')
    x,y = app.gunfire[0]
    r,t = app.gunfire[1]
    canvas.create_line(x,y,r,t,width = 3)    
    


runApp(width = 1280, height =747)


    
    
