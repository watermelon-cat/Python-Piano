import pygame
pygame.init()#initializes Pygame
pygame.display.set_caption("python piano program")#sets the window title
screen = pygame.display.set_mode((1100, 800))#creates game screen
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
press = False

#audio stuff!
pygame.mixer.init()
k1 = pygame.mixer.Sound("key01.mp3")
k3 = pygame.mixer.Sound("key03.mp3")
k5 = pygame.mixer.Sound("key05.mp3")
k7 = pygame.mixer.Sound("key07.mp3")
k9 = pygame.mixer.Sound("key09.mp3")
k11 = pygame.mixer.Sound("key11.mp3")
k13 = pygame.mixer.Sound("key13.mp3")
k15 = pygame.mixer.Sound("key15.mp3")
k17 = pygame.mixer.Sound("key17.mp3")
k19 = pygame.mixer.Sound("key19.mp3")
k21 = pygame.mixer.Sound("key21.mp3")
k23 = pygame.mixer.Sound("key23.mp3")

k2 = pygame.mixer.Sound("key02.mp3")
k4 = pygame.mixer.Sound("key04.mp3")
k6 = pygame.mixer.Sound("key06.mp3")
k8 = pygame.mixer.Sound("key08.mp3")
k10 = pygame.mixer.Sound("key10.mp3")
k12 = pygame.mixer.Sound("key12.mp3")
k14 = pygame.mixer.Sound("key14.mp3")
k16 = pygame.mixer.Sound("key16.mp3")


#this holds onto what key the user has pressed
key = 0

#gameloop###################################################
while True:
    print(mousePos) #this is just for testing so you can see the mouse coordinates on the screen!
    
    #event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
    
    #update/timer section---------------------------------------
    if mousePos[0] > 75 and mousePos[0] < 125 and mousePos[1] >500 and mousePos[1] < 650:
        key = 2
    elif mousePos[0] > 175 and mousePos[0] < 225 and mousePos[1] >500 and mousePos[1] < 650:
        key = 4
    elif mousePos[0] > 275 and mousePos[0] < 325 and mousePos[1] >500 and mousePos[1] < 650:
        key = 6
    elif mousePos[0] > 475 and mousePos[0] < 525 and mousePos[1] >500 and mousePos[1] < 650:
        key = 8
    elif mousePos[0] > 575 and mousePos[0] < 625 and mousePos[1] >500 and mousePos[1] < 650:
        key = 10
    elif mousePos[0] > 775 and mousePos[0] < 825 and mousePos[1] >500 and mousePos[1] < 650:
        key = 12
    elif mousePos[0] > 875 and mousePos[0] < 925 and mousePos[1] >500 and mousePos[1] < 650:
        key = 14
    elif mousePos[0] > 975 and mousePos[0] < 1025 and mousePos[1] >500 and mousePos[1] < 650:
        key = 16
    elif mousePos[0] > 0 and mousePos[0] < 100 and mousePos[1] >500:
        key = 1
    elif mousePos[0] > 100 and mousePos[0] < 200 and mousePos[1] >500:
        key = 3
    elif mousePos[0] > 200 and mousePos[0] < 300 and mousePos[1] >500:
        key = 5
    elif mousePos[0] > 300 and mousePos[0] < 400 and mousePos[1] >500:
        key = 7
    elif mousePos[0] > 400 and mousePos[0] < 500 and mousePos[1] >500:
        key = 9
    elif mousePos[0] > 500 and mousePos[0] < 600 and mousePos[1] >500:
        key = 11
    elif mousePos[0] > 600 and mousePos[0] < 700 and mousePos[1] >500:
        key = 13
    elif mousePos[0] > 700 and mousePos[0] < 800 and mousePos[1] >500:
        key = 15
    elif mousePos[0] > 800 and mousePos[0] < 900 and mousePos[1] >500:
        key = 17
    elif mousePos[0] > 900 and mousePos[0] < 1000 and mousePos[1] >500:
        key = 19
    elif mousePos[0] > 1000 and mousePos[0] < 1100 and mousePos[1] >500:
        key = 21
    elif mousePos[0] > 1100 and mousePos[0] < 1200 and mousePos[1] >500:
        key = 23
    #add more keys here!
    else:
        key = 0
    
    #input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        press = True

    if event.type == pygame.MOUSEBUTTONUP:
        press = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos


    #render section---------------------------------------------

    #the keys 
    pygame.draw.rect(screen, (255, 255, 255), (0, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (100, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (200, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (300, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (400, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (500, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (600, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (700, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (800, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (900, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (1000, 500, 100, 300))
    pygame.draw.rect(screen, (255, 255, 255), (1100, 500, 100, 300))
    
    #black keys
    pygame.draw.rect(screen, (0, 0, 0), (75, 500, 50, 150))
    pygame.draw.rect(screen, (0, 0, 0), (175, 500, 50, 150))
    pygame.draw.rect(screen, (0, 0, 0), (275, 500, 50, 150))
    pygame.draw.rect(screen, (0, 0, 0), (475, 500, 50, 150))
    pygame.draw.rect(screen, (0, 0, 0), (575, 500, 50, 150))
    pygame.draw.rect(screen, (0, 0, 0), (775, 500, 50, 150))
    pygame.draw.rect(screen, (0, 0, 0), (875, 500, 50, 150))
    pygame.draw.rect(screen, (0, 0, 0), (975, 500, 50, 150))
    
    #key outlines
    pygame.draw.rect(screen, (0, 0, 0), (0, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (100, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (200, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (300, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (400, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (500, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (600, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (700, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (800, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (900, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (1000, 500, 100, 300), 2)
    pygame.draw.rect(screen, (0, 0, 0), (1100, 500, 100, 300), 2)
    
    
    #if a key is pressed, highlight in grey and play the sound:
    if press == True:
        if key == 0:
            print("no key")
        elif key == 1:
            pygame.mixer.Sound.play(k1)
            pygame.draw.rect(screen, (150,150,150), (0,500,100,300))
        elif key == 3:
            pygame.mixer.Sound.play(k3)
            pygame.draw.rect(screen, (150,150,150), (100,500,100,300))
        elif key == 5:
            pygame.mixer.Sound.play(k5)
            pygame.draw.rect(screen, (150,150,150), (200,500,100,300))
        elif key == 7:
            pygame.mixer.Sound.play(k7)
            pygame.draw.rect(screen, (150,150,150), (300,500,100,300))
        elif key == 9:
            pygame.mixer.Sound.play(k9)
            pygame.draw.rect(screen, (150,150,150), (400,500,100,300))
        elif key == 11:
            pygame.mixer.Sound.play(k11)
            pygame.draw.rect(screen, (150,150,150), (500,500,100,300))
        elif key == 13:
            pygame.mixer.Sound.play(k13)
            pygame.draw.rect(screen, (150,150,150), (600,500,100,300))
        elif key == 15:
            pygame.mixer.Sound.play(k15)
            pygame.draw.rect(screen, (150,150,150), (700,500,100,300))
        elif key == 17:
            pygame.mixer.Sound.play(k17)
            pygame.draw.rect(screen, (150,150,150), (800,500,100,300))
        elif key == 19:
            pygame.mixer.Sound.play(k19)
            pygame.draw.rect(screen, (150,150,150), (900,500,100,300))
        elif key == 21:
            pygame.mixer.Sound.play(k21)
            pygame.draw.rect(screen, (150,150,150), (1000,500,100,300))
        elif key == 23:
            pygame.mixer.Sound.play(k23)
            pygame.draw.rect(screen, (150,150,150), (1100,500,100,300))
        elif key == 2:
            pygame.mixer.Sound.play(k2)
            pygame.draw.rect(screen, (150,150,150), (75,500,50,150))
            print("key 2")
        elif key == 4:
            pygame.mixer.Sound.play(k4)
            pygame.draw.rect(screen, (150,150,150), (175,500,50,150))
        elif key == 6:
            pygame.mixer.Sound.play(k6)
            pygame.draw.rect(screen, (150,150,150), (275,500,50,150))
        elif key == 8:
            pygame.mixer.Sound.play(k8)
            pygame.draw.rect(screen, (150,150,150), (475,500,50,150))
        elif key == 10:
            pygame.mixer.Sound.play(k10)
            pygame.draw.rect(screen, (150,150,150), (575,500,50,150))
        elif key == 12:
            pygame.mixer.Sound.play(k12)
            pygame.draw.rect(screen, (150,150,150), (775,500,50,150))
        elif key == 14:
            pygame.mixer.Sound.play(k14)
            pygame.draw.rect(screen, (150,150,150), (875,500,50,150))
        elif key == 16:
            pygame.mixer.Sound.play(k16)
            pygame.draw.rect(screen, (150,150,150), (975,500,50,150))
    
    
    pygame.display.flip() #always needed at the end of every game loop!
    

#end game loop##############################################

pygame.quit()
