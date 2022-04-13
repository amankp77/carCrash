from cmath import sqrt
from ctypes.wintypes import RGB
import math
from operator import iconcat
from random import randint, random
import sys
from telnetlib import SGA
from turtle import Screen
from pygame.locals import *
import pygame 
import time

pygame.init()

screen = pygame.display.set_mode((540,750))
pygame.display.set_caption("Car-Crash")


# ------------------------------------ music -------------------------------------
pygame.mixer.init()
pygame.mixer.music.load('music/bgm.mp3')
pygame.mixer.music.play(-1)


playing = False

# images ---------------------------------sprite-------------------------------------
user = pygame.image.load('img/user.png')
icon = pygame.image.load('img/user.jpg')
pygame.display.set_icon(icon)
road = pygame.image.load('img/road.png').convert()
enemies = []
blast = pygame.image.load('img/BLAST.png')
font = pygame.font.Font('font/font.ttf', 40)




carX = None
carY = None
carX_Change = None
carY_Change = None

enemyX = None
enemyX_C = None
enemyY_C = None
enemyY = None
enemyY_change = None
xCounterList = None
yCounterList = None
enemyY_Level = None

Score = 0
score = font.render(f"Score : {Score}", 1, (255,255,255))
Highscore = 0
hiscore = font.render(f"HighScore : {Highscore}", 1, (255,255,255))


# font = pygame.font.Font(None, 36)
# text = font.render("Hello There", 1, (10, 10, 10))
# textpos = text.get_rect()


def check():
    global xCounterList, enemyX_C, font , screen , user , road   , enemies , blast , carX , carY , carX_Change , carY_Change , enemyX , enemyY , enemyY_change , playing
    idx = 0
    for e in enemies:
        if math.sqrt(((enemyX[idx]-carX)**2) + ((enemyY[idx]-carY)**2)) < 70.0:
            collision_sound = pygame.mixer.Sound("music/explosion.wav")
            collision_sound.play()
            playing = False
            Score = 0
            return "Not"
        idx = idx + 1


def main():
    
    global xCounterList, enemyX_C, font , screen ,user , road   , enemies , blast , carX , carY , carX_Change , carY_Change , enemyX , enemyY , enemyY_change ,playing , score , Score , Highscore, hiscore, enemyY_C , yCounterList, enemyY_Level

    if playing: 
     while 1:  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    carY_Change = -0.2
                if event.key == pygame.K_DOWN:
                    carY_Change = 0.2
                if event.key == pygame.K_LEFT:
                    carX_Change = -0.2
                if event.key == pygame.K_RIGHT:
                    carX_Change = 0.2
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    carX_Change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    carY_Change = 0
        if carX<10:
            carX = 10
        elif carX > 450:
            carX = 450


        if carY<130:
            carY = 130
        elif carY > 640:
            carY = 640
        
        carX = carX + carX_Change
        carY = carY + carY_Change
    
    
        screen.blit(road, (0,0))
        screen.blit(user ,(carX,carY))
        idx = 0
        for e in enemies:
            screen.blit(e,(enemyX[idx],enemyY[idx]))
            idx = idx + 1
    
        for i in range(len(enemies)):
            enemyY[i] = enemyY[i] + enemyY_change
            if(enemyY[i]>700):
                Score += 1
                score = font.render(f"Score : {Score}", 1, (255,255,255))




# -----------------------------------------------Level -----------------------------------------

                if Score>30:
                    enemyY_change = enemyY_Level[1]
                if Score>100:
                    enemyY_change = enemyY_Level[2]
                if Score>140:
                    enemyY_change = enemyY_Level[3]
                if Score>180:
                    enemyY_change = enemyY_Level[4]



# -----------------------------------------------Level -----------------------------------------

                if Score>Highscore:
                    hiscore = font.render(f"HighScore : {Score}", 1, (255,255,255))
                    with open('Highscore.txt','w') as f:
                        f.write(str(Score))
                if(len(yCounterList)==0):
                    yCounterList = [0,1,2,3,4,5,6]
                l = yCounterList.pop(randint(0,len(yCounterList)-1))
                enemyY[i] = enemyY_C[l] 
                if(len(xCounterList)==0):
                    xCounterList = [0,1,2,3,4,5,6]
                l = xCounterList.pop(randint(0,len(xCounterList)-1))
        
                # enemyX[i] = enemyX_C[l]
                screen.blit(enemies[i],(enemyX[i],enemyY[i]))
                
    
        status = check()

        if(status is "Not"):
            screen.blit(blast,(carX,carY))
            pygame.display.update()
            time.sleep(0.2)
            Score = 0
            return
        
        screen.blit(score,(350,0)) 
        screen.blit(hiscore,(10,0))    
        pygame.display.update()
        

    else:
        xCounterList = [0,1,2,3,4,5,6]
        yCounterList = [0,1,2,3,4,5,6]
        user = pygame.image.load('img/user.png').convert_alpha()
        road = pygame.image.load('img/road.png').convert_alpha()
        enemies = []
        enemies.append(pygame.image.load('img/enemy1.png').convert_alpha())
        enemies.append(pygame.image.load('img/enemy2.png').convert_alpha())
        enemies.append(pygame.image.load('img/enemy3.png').convert_alpha())
        enemies.append(pygame.image.load('img/enemy4.png').convert_alpha())
        enemies.append(pygame.image.load('img/enemy3.png').convert_alpha())
        enemies.append(pygame.image.load('img/enemy4.png').convert_alpha())
        enemies.append(pygame.image.load('img/enemy5.png').convert_alpha())
        blast = pygame.image.load('img/BLAST.png')
        carX = 270
        carY = 635
        carX_Change = 0
        carY_Change = 0
        enemyX = [20,150,280,420,150,20,280]
        enemyX_C = [20,150,280,420,150,20,280]
        enemyY = [10,-140,160,-280,-410,300,-550]
        enemyY_C = [-300,-440,-160,-580,-710,0,-850]
        enemyY_Level = [0.1,0.2,0.3,0.5,1]
        enemyY_change = enemyY_Level[0]
        Score = 0
        with open('Highscore.txt','r') as f:
            Highscore = int(f.readline())

        hiscore = font.render(f"HighScore : {Highscore}", 1, (255,255,255))
        
         
        while 1:
             for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if ( pygame.Rect((123,335,300,100)).collidepoint(pygame.mouse.get_pos())):
                 if event.type == pygame.MOUSEBUTTONDOWN:
                     playing = True
                     return
             screen.blit(road,(0,0))
             play = font.render("Play Car-Crash", 1, (0,0,0))
             white = pygame.image.load('img/white.png')
             screen.blit(white,(125,335))
             screen.blit(play,(150,350))
             pygame.display.update()
            #  print(white.get_rect())
            

             

# start()
while 1: 
    main()