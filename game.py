import pygame
pygame.init()

win = pygame.display.set_mode((602,602))

turn = 1 #even turn = cross and odd turn = circle
status = [0 for i in range(9)] #0 for empty o for circle and x for cross

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
            if(turn & 1):
                win.blit(pygame.image.load('circle.png'),((pos[0]//200)*200,(pos[1]//200)*200))
                status[3*(pos[1]//200)+(pos[0]//200)] = 'o'
                print(status)
            else:
                win.blit(pygame.image.load('cross.png'),((pos[0]//200)*200,(pos[1]//200)*200))
                status[3*(pos[1]//200)+(pos[0]//200)] = 'x'
            turn = turn + 1


    pygame.draw.lines(win, (255,255,255), False, [(200,0),(200,601)], 1)
    pygame.draw.lines(win, (255,255,255), False, [(401,0),(401,602)], 1)
    pygame.draw.lines(win, (255,255,255), False, [(0,200),(602,200)], 1)
    pygame.draw.lines(win, (255,255,255), False, [(0,401),(602,401)], 1)



    pygame.display.update()