import pygame as pg
from pygame import mixer
import sys 
from pygame.locals import *
import random
import math
import time
pg.init()
pg.font.init()  
pg.font.get_init()
cursor_img = pg.image.load('cursor.png')
# pygame setup
WHITE = 255,255,255
clock = pg.time.Clock()
screen = pg.display.set_mode((1440,900))
start = 0
sec = 3
pause = 0
p9 = 0
gravity = 0.17
width = 30
height = 40
#pg.mouse.set_visible(False)
fruits = [pg.image.load("guava.png"), pg.image.load("melon.png"), pg.image.load("pomegranate.png"), pg.image.load("orange.png"), pg.image.load("bomb.png")]
font1 = pg.font.SysFont('Chalkduster', 100)
font2 = pg.font.SysFont('Chalkduster', 150)
font3 = pg.font.SysFont('Chalkduster', 100)
font4 = pg.font.SysFont('Chalkduster', 50)
font5 = pg.font.SysFont('Chalkduster', 40)
text1 = font1.render('Press SPACE to start', True, (255, 255, 255))
text2 = font2.render('START in ' + str(sec), True, (255, 255, 255))
text3 = font3.render('PAUSED', True, (255, 255, 255))
text4 = font2.render('START!', True, (255, 255, 255))
text5 = font5.render('Press SPACE to resume, Press Q to go to the menu', True, (WHITE))
textRect2 = text2.get_rect()
textRect2.center = (700, 500)
textRect1 = text1.get_rect()
textRect1.center = (700, 500)
textRect3 = text3.get_rect()
textRect3.center = (700, 500)
textRect4 = text4.get_rect()
textRect4.center = (700, 500)
textRect5 = text5.get_rect()
textRect5.center = (700, 600)
running = True
pg.mixer.init()
pg.mixer.music.load("fruitninja_music.wav")
pg.mixer.music.set_volume(0.7)
pg.mixer.music.play()
pg.display.set_caption('Fruit Ninja')
logo = pg.image.load("fruitninja_logo.png")
background = pg.image.load("fruitninja_background.png")
def paused():
    screen.fill(WHITE)
    screen.blit(background,(0,0))
    screen.blit(logo,(364,100))
    screen.blit(text3, textRect3)
    screen.blit(text5, textRect5)
    pause = 1
def score(add, minus):
    scr = 0
    scr += add
    scr -= minus
    scr_txt = font4.render('Score: ' + str(scr), True, (WHITE))
    textRectscr = scr_txt.get_rect()
    textRectscr.center = (110, 20)
    screen.blit(scr_txt, textRectscr)
    
def fruit(speed):
    x = random.uniform(0, 1440)
    y = 900
    fruit = random.choice(fruits)
    screen.blit(fruit,(x, y))
    screen.blit(background(0, 0))
    score(0, 0)
    screen.blit(fruit,(x, y))
    x_stop_left = random.uniform(75, 330)
    x_stop_right = random.uniform(1075, 1315)
    x_stop = random.choice(x_stop_right, x_stop_left)
    y_boundary = random.uniform(330, 150)
    screen.blit(fruit(x, y))
    
screen.blit(background,(0,0))
screen.blit(logo,(364,100))
screen.blit(text1, textRect1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
            
        
    # fill the screen with a color to wipe away anything from last frame
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                pause = 0
                text2 = font2.render('START in ' + str(sec), True, (255, 255, 255))
                for i in range(3):
                    screen.blit(background,(0,0))
                    screen.blit(text2, textRect2)
                    screen.blit(logo,(364,100))
                    pg.time.delay(1000)
                    sec -= 1
                    text2 = font2.render('START in ' + str(sec), True, (255, 255, 255))
                    pg.display.update()
                pg.time.delay(1000)
                screen.blit(background,(0,0))
                screen.blit(text4, textRect4)
                pg.display.update()
                pg.time.delay(1000)
                screen.blit(background,(0,0))
                pg.display.update()
                sec = 3
                score(0, 0)
                start = 1
                   
            if event.key == pg.K_TAB:
                paused()
                
            if event.key == pg.K_q:
                pg.mixer.music.load("fruitninja_music.wav")
                pg.mixer.music.set_volume(0.7)
                pg.mixer.music.play()
                screen.blit(background,(0,0))
                screen.blit(logo,(364,100))
                screen.blit(text1, textRect1)

    #gameplay
    if pause != 1:
        if start == 1:
            score(0, 0)
    mouse_pos = pg.mouse.get_pos()
    mouse_pos += 200, 200
    #screen.blit(background,(0, 0))
    pg.display.update()
    screen.blit(cursor_img,(mouse_pos))
    pg.display.update()        

    pg.display.update()
