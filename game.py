import pygame
pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

isEnd = False
turn = 1 #even turn = cross and odd turn = circle
status = [0 for i in range(9)] #0 for empty o for circle and x for cross

def winMsg(a):
    if a == 1:
        textsurface = myfont.render('cross wins' , False, (255, 255, 255))
        
    if a == 2:
        textsurface = myfont.render('circle wins' , False, (255, 255, 255))
        
    if a == 3:
        textsurface = myfont.render('its a tie' , False, (255, 255, 255))
        
    if a == 4:
        textsurface = myfont.render('' , False, (255, 255, 255))

    win.blit(textsurface,(0,0))

 
def checkWin(status):
    global isEnd
    j = 0
    for i in status:
        if i == 0:
            j += 1

    if((status[0] == status[1] == status[2] == 'x') 
    or (status[3] == status[4] == status[5] == 'x') 
    or (status[6] == status[7] == status[8] == 'x')
    or (status[0] == status[3] == status[6] == 'x')
    or (status[1] == status[4] == status[7] == 'x')
    or (status[2] == status[5] == status[8] == 'x')
    or (status[0] == status[4] == status[8] == 'x')
    or (status[2] == status[4] == status[6] == 'x')): 
        isEnd = True
        return 1
        

    elif((status[0] == status[1] == status[2] == 'o') 
    or (status[3] == status[4] == status[5] == 'o') 
    or (status[6] == status[7] == status[8] == 'o')
    or (status[0] == status[3] == status[6] == 'o')
    or (status[1] == status[4] == status[7] == 'o')
    or (status[2] == status[5] == status[8] == 'o')
    or (status[0] == status[4] == status[8] == 'o')
    or (status[2] == status[4] == status[6] == 'o')): 
        isEnd = True
        return 2
        

    elif(j == 0):
        return 3
    else:
        return 4
    

def displayImg(s, c): #to display cross or circle on click
    win.blit(pygame.image.load(s),((pos[0]//200)*200,(pos[1]//200)*200))
    status[3*(pos[1]//200)+(pos[0]//200)] = c

win = pygame.display.set_mode((602,602))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if isEnd == False:

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                if(turn & 1):
                    displayImg('circle.png', 'o')
                    winMsg(checkWin(status))
                    
                else:
                    displayImg('cross.png','x')
                    winMsg(checkWin(status))
                        
                turn = turn + 1


    pygame.draw.lines(win, (255,255,255), False, [(200,0),(200,601)], 1)
    pygame.draw.lines(win, (255,255,255), False, [(401,0),(401,602)], 1)
    pygame.draw.lines(win, (255,255,255), False, [(0,200),(602,200)], 1)
    pygame.draw.lines(win, (255,255,255), False, [(0,401),(602,401)], 1)


    pygame.display.update()