import pygame as pg
import sys, os
from pygame.locals import *
pg.init()
draw = 0
color = 0
thick = 30
sav = 0
c = 0
r = 0
g = 0
b = 0
l = 0
n = 0
z = 0
i9 = 1
long = 0
k9 = 0
a = 255
surf = pg.image.load('dot.png') # you could also load an image 
surf.fill((r,g,b))        # and use that as your surface
color_cur = pg.cursors.Cursor((thick+20, thick+20), surf)
drawing_name = ''
load_name = ''
th = False
circle_pos_lst = []
WHITE = 255,255,255
i8 = 0
file = 0
screen = pg.display.set_mode((1440,900),pg.FULLSCREEN,pg.SCALPHA)
pg.display.set_caption('Desktop Procreate')
screen.fill(WHITE)
pg.mouse.set_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)
pg.mouse.set_cursor(color_cur)
#pg.mouse.set_visible(False)
font1 = pg.font.SysFont('Chalkduster', 50)
font2 = pg.font.SysFont('Chalkduster', 25)
text1 = font1.render('What do you want to name your artwork:', True, (0, 0, 0))
textRect1 = text1.get_rect()
textRect1.center = (700, 500)
text2 = font1.render(drawing_name, True, (0, 0, 0))
textRect2 = text2.get_rect()
textRect2.center = (700, 500)
text3 = font1.render('Too Long!', True, (0, 0, 0))
textRect3 = text3.get_rect()
textRect3.center = (700, 700)
text4 = font1.render('What do artwork do you want to load:', True, (0, 0, 0))
textRect4 = text4.get_rect()
textRect4.center = (700, 500)
text5 = font1.render(load_name, True, (0, 0, 0))
textRect5 = text5.get_rect()
textRect5.center = (700, 600)
text6 = font2.render('Not a drawing!', True, (0, 0, 0))
textRect6 = text6.get_rect()
textRect6.center = (700, 700)
line_pos_lst = []
def save():
    global sav
    sav += 1
    screen.blit(text1, textRect1)
while True:
    fill = r,g,b
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if sav % 2 == 0:
                    screen.fill(WHITE)
            if event.key == pg.K_TAB:
                if sav % 2 == 0:
                    draw += 1
                    pg.mouse.set_visible(True)
            if event.key == pg.K_p:
                if sav % 2 == 0:
                    r = 255
                    g = 255
                    b = 255
                    a = 255
                    color += 1
            if event.key == pg.K_0:
                if sav % 2 == 0:
                    thick = 5
            if event.key == pg.K_1:
                if sav % 2 == 0:
                    thick = 10
            if event.key == pg.K_2:
                if sav % 2 == 0:
                    thick = 20
            if event.key == pg.K_3:
                if sav % 2 == 0:
                    thick = 30
            if event.key == pg.K_4:
                if sav % 2 == 0:
                    thick = 40
            if event.key == pg.K_5:
                if sav % 2 == 0:
                    thick = 50
            if event.key == pg.K_q:
                if sav % 2 == 0:
                    color1 = [r,g,b,a]
            if event.key == pg.K_w:
                if sav % 2 == 0:
                    color2 = [r,g,b,a]
            if event.key == pg.K_e:
                if sav % 2 == 0:
                    color3 = [r,g,b,a]
            if event.key == pg.K_a:
                if sav % 2 == 0:
                    r = color1[0]
                    g = color1[1]
                    b = color1[2]
                    a = color1[3]
            if event.key == pg.K_s:
                if sav % 2 == 0:
                    r = color2[0]
                    g = color2[1]
                    b = color2[2]
                    a = color2[3]
            if event.key == pg.K_d:
                if sav % 2 == 0:
                    r = color3[0]
                    g = color3[1]
                    b = color3[2]
                    a = color3[3]
            if event.key == pg.K_m:
                if sav % 2 == 0:
                    screen.fill(fill)
            if event.key == pg.K_c:
                if sav % 2 == 0:
                    r = 0
                    g = 0
                    b = 0
                    a = 255
            if event.key == pg.K_r:
                if sav % 2 == 0:
                    r += 10
            if event.key == pg.K_g:
                if sav % 2 == 0:
                    g += 10
            if event.key == pg.K_b:
                if sav % 2 == 0:
                    b += 10
            if event.key == pg.K_F4:
                pg.image.save(screen, '/Users/mac/Desktop/python projects/desktop procreate/temp' + str(i9) + '.png')
                save()
                a += 1
                std = True
                while std:
                    pg.draw.rect(screen, (255,255,255), Rect(100, 400, 1240, 400))
                    text2 = font1.render(drawing_name, True, (0, 0, 0))
                    textRect2 = text2.get_rect()
                    textRect2.topleft = (300,600)
                    screen.blit(text2, textRect2)
                    save()
                    if len(drawing_name) == 30:
                        screen.blit(text3, textRect3)
                        long = 1
                    else:
                        long = 0
                    for event in pg.event.get():
                        if event.type == KEYDOWN:
                            if event.key == pg.K_BACKSPACE:
                                drawing_name = drawing_name[:-1]
                            elif event.key == pg.K_RETURN:
                                a9 = pg.image.load('temp' + str(i9) + '.png')
                                screen.blit(a9,(0,0))
                                pg.image.save(screen, 'procreate_drawing_' + drawing_name + ".png")
                                drawing_name = ''
                                std = False
                            else:
                                if long == 0:
                                    if event.unicode == ' ':
                                        drawing_name += '_'
                                    else:
                                        drawing_name += event.unicode
                    pg.display.update()
                sav += 1
                screen.fill((255,255,255))
                continue
            if event.key == pg.K_F6:
                screen.blit(text4, textRect4)
                sav += 1
                th = True
                while th:
                    pg.draw.rect(screen, (255,255,255), Rect(100, 400, 1240, 400))
                    screen.blit(text4, textRect4)
                    screen.blit(text5, textRect5)
                    text5 = font1.render(load_name, True, (0, 0, 0))
                    textRect5 = text5.get_rect()
                    textRect5.center = (700, 600)
                    if len(load_name) == 30:
                        screen.blit(text3, textRect3)
                        long = 1
                    else:
                        long = 0
                    if file == 1:
                        screen.blit(text6, textRect6)
                    if os.path.isfile('procreate_drawing_' + load_name + '.png') == True:
                        file = 0
                    for event in pg.event.get():
                        if event.type == KEYDOWN:
                            if event.key == pg.K_BACKSPACE:
                                load_name = load_name[:-1]
                            elif event.key == pg.K_RETURN:
                                if os.path.isfile('procreate_drawing_' + load_name + '.png') == True:
                                    z0 = pg.image.load('procreate_drawing_' + load_name + '.png')
                                    screen.blit(z0,(0,0))
                                    load_name = ''
                                    th = False
                                else:
                                    file = 1 
                            else:
                                if long == 0:
                                    if event.unicode == ' ':
                                        load_name += '_'
                                    else:
                                        load_name += event.unicode
                    pg.display.update()
                continue
            if event.key == pg.K_F9:
                c += 1
                pg.mouse.set_visible(True)
                circle_pos_lst.append(pg.mouse.get_pos())
                if len(circle_pos_lst) == 2:
                    x1,y1 = circle_pos_lst[0]
                    x2,y2 = circle_pos_lst[1]
                    radius = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
                    pg.draw.circle(screen, (r,g,b),[x1,y1], radius, thick)
                    circle_pos_lst.clear()
                    print(x1,y1,x2,y2)
            if event.key == pg.K_l:
                if sav % 2 == 0:
                    pg.mouse.set_visible(True)
                    c += 1
                    l += 1
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            line_pos_lst.append(pg.mouse.get_pos())
            l += 1
            if len(line_pos_lst) == 2:
                pg.draw.line(screen, (r,g,b,a), line_pos_lst[0], line_pos_lst[1], width=thick)
                print(line_pos_lst[0],line_pos_lst[1])
                n += 1
                line_pos_lst.clear()
        
    if draw % 2 == 0:
        if c % 2 == 0:
            if color % 2 != 1:
                pg.mouse.set_visible(False)
                r %= 255
                g %= 255
                b %= 255
                a %= 255
            x,y = pg.mouse.get_pos()
            pg.draw.circle(screen, (r,g,b,a),[x, y], thick, 0)
    pg.display.update()
