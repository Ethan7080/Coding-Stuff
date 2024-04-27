import pygame, datetime, sys, time, pickle
pygame.init()
date = datetime.datetime.now().strftime("%Y-%m-%d")
time = datetime.datetime.now().strftime("%H:%M:%S")
font2 = pygame.font.SysFont('Arial', 100)
font1 = pygame.font.SysFont('Arial', 55)
timertxt = font2.render('   :    :   ', True, (0, 0, 0))
timertxtRect1 = timertxt.get_rect()
timertxtRect1.center = (250, 150)
screen = pygame.display.set_mode((500,300),pygame.RESIZABLE)
screen.fill("White")
page = 1
start_timer = ''
running= True
def time():
    screen.fill('White')
    date = font1.render(datetime.datetime.now().strftime("%Y-%m-%d"), True, (0, 0, 0))
    time = font2.render(datetime.datetime.now().strftime("%H:%M:%S"), True, (0, 0, 0))
    timeRect1 = time.get_rect()
    timeRect1.center = (250, 100)
    dateRect1 = date.get_rect()
    dateRect1.center = (250, 200)
    screen.blit(date, dateRect1)
    screen.blit(time, timeRect1)
    pygame.display.update()
def timer():
    my_time = ''
    typing = True
    while typing:
        screen.fill('White')
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    my_time = drawing_name[:-1]
                num = event.unicode
                if num.isdigit():
                    my_time += num
                if len(my_time) == 2 or len(my_time) == 5:
                    my_time += ' '
                if len(my_time) == 8:
                    typing = False
        txt = font2.render(my_time, True, (0, 0, 0))
        txtRect1 = txt.get_rect()
        txtRect1.midleft = (60,160)
        screen.blit(txt, txtRect1)
        screen.blit(timertxt, timertxtRect1)
        pygame.display.update()
    start_timer = my_time
        
    
   
while running:
    if page == 0:
        page = 1
    if page == 5:
        page = 4
    if page == 1:
        time()
    if page == 2:
        timer()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mouse.set_pos(150,250)
            pygame.display.quit()
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                page -= 1
            if event.key == pygame.K_RIGHT:
                page += 1
    pygame.display.update()
    
    
    
        
    
