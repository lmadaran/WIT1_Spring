## THIS IS A PROGRAM THAT WILL HAVE A BLUE RECTANGLE IN THE CENTER, WITH A RED BACKGROUND ##

#IMPORTING THE PYGAME MODULE
import pygame 

#THIS ENSURES THAT THE GAME WILL START
pygame.init() 

#WE WILL CREATE VARIABLES WITH COLOR NAMES SO WE CAN USE THEM LATER ON
blue = (0, 0, 255)
red = (255, 0, 0)

#HOW MANY PIXELS WIDE AND TALL OUR GAME WINDOW IS
screenWidth = 400 
screenHeight = 500 

#X AND Y LOCATIONS OF OUR RECTANGLE. NOTICE THAT IT IS HALF THE DIMENSIONS OF THE SCREEN, SO IT WILL ORIGINATE IN THE CENTER
rectX = screenWidth / 2
rectY = screenHeight / 2

#CREATING OUR ACTUAL GAME WINDOW DISPLAY; IT IS CALLED 'screen'
screen = pygame.display.set_mode((screenWidth, screenHeight)) 

#THIS IS NECESSARY FOR WHEN WE WANT TO SHUT OFF OUR INFINITE WHILE LOOP
gameOff = False 

#DELAYING OUR PROGRAMING SO THAT ONLY A CERTAIN AMOUNT OF FPS WILL BE DISPLAYED
clock = pygame.time.Clock()
FPS = 60

jumpState = False
jumpCount = jumpLimit = 8

glideState = False
posStart = rectY
#THIS WHILE LOOP WILL REPEAT OVER AND OVER, AND MAKE SURE THAT OUR GAME VISUALS ARE CONSTANTLY UPDATING
while not gameOff: 
  
    clock.tick(FPS)

  #THIS IS NECESSARY TO CAPTURE THE EVENTS THAT ARE HAPPENING IN OUR GAME
    for event in pygame.event.get(): 
    
        #IF THE EVENT IS PRESSING THE 'X' BUTTON IN THE TOP LEFT OF THE SCREEN, THEN CLOSE 
        if event.type == pygame.QUIT: 
            gameOff = True #TURN OFF THE INFINITE WHILE LOOP
            pygame.quit() #SHUT OFF THE PROGRAM

          
        #IF THIS EVENT DETECTS ANY KEY BEING PRESSED, WE WILL EXECUTE THE PROGRAM BELOW:
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_SPACE: #PRESSING THE SPACEBAR KEY 
                jumpState = True #INITIATE THE STATE OF JUMPING
    
    #THE CODE BELOW WILL MAKE IT SO THE RECTANGLE MOVES WHEN WE HOLD DOWN A KEY

    #WE START OF BY CREATING A VARIABLE THAT WILL CAPTURE WHEN KEYS ARE PRESSED
    keyPress = pygame.key.get_pressed()
    if keyPress[pygame.K_a]: #WE THEN TEST IF THE KEY BEING HELD DOWN IS A OR D
        rectX -= 20 #IF KEY A IS HELD DOWN, MOVE LEFT CONTINOUSLY
    elif keyPress[pygame.K_d]:
        rectX += 20 #IF KEY D IS HELD DOWN, MOVE RIGHT CONTINOUSLY
    elif keyPress[pygame.K_SPACE]:
            rectY += 1
            glideState = True

    if jumpState and jumpCount >= -jumpLimit:
        if jumpCount > 0:
            rectY -= jumpCount**2
        elif jumpCount < 0 and not glideState:
            rectY += jumpCount**2
        jumpCount -= 1
    else:
        jumpCount = jumpLimit
        jumpState = False

    
    screen.fill((red)) #THIS IS WHERE WE SET THE BACKGROUND COLOR TO RED
    pygame.draw.rect(screen, blue, (rectX, rectY, 100, 100), 0) #THIS IS WHERE WE CREATE A RECTANGLE
    pygame.display.update()
  
