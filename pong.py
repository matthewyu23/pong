import pygame #imports pygame

pygame.init() #initializes all the modules required for PyGame

screen = pygame.display.set_mode((400, 300)) #this will launch a window, the return value is a Surface object which is the object you will perform graphical operations on

done = False #keeps the window open

is_blue = True
clock = pygame.time.Clock() #creates clock object to control framerate
w, h = pygame.display.get_surface().get_size() #getting the window dimensions
x = h/2
y = h/2

a = w/5
b = w/3
av = 3
bv = 3
score = 0

while not done: #the main loop

    pygame.display.set_caption('Pong') #sets the title of the window

    for event in pygame.event.get(): #checks events
            if event.type == pygame.QUIT: 
                    done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                is_blue = not is_blue
    

    pressed = pygame.key.get_pressed() #controling paddles
    if pressed[pygame.K_w] and x >= 0: x -= 3
    if pressed[pygame.K_s] and x <= h - 60: x += 3
    if pressed[pygame.K_UP] and y >= 0: y -= 3
    if pressed[pygame.K_DOWN] and y <= h - 60: y += 3
    
    a += av
    b += bv

    if a >= w-10 or a<=0: av = -av #bounce on walls
    if b >= h-10 or b<=0: bv = -bv

    if a <= w/15 + 10 and b >= x and b <= x + 60: #bounce on paddles, add score, increase speed
        av = -av 
        score = score + 1
        av = av * 1.25
        bv = bv * 1.25
    if a >= w - w/15 - 20 and b >= y and b <= y + 60: 
        av = -av
        score = score + 1
        av = av * 1.1
        bv = bv * 1.1

    if a <= 0 or a >= w-10: #resets score and speed
        score = 0
        pygame.time.delay(1000)
        a = w/5
        b = w/3
        av = 3
        bv = 3

    font = pygame.font.Font('freesansbold.ttf', 32) #creats a font object
    text = font.render(str(score), True, (255, 255, 255), (0, 0, 0)) #creates a text object from the font object
    textRect = text.get_rect() #creates rectangular object behind the text
    textRect.center = (w/ 2, h / 2) #centers the rectangular object 
    screen.blit(text, textRect) #copyies the text surface object to the display surface object 

    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(w/15, x, 10, 60)) #draws a rectangle, parameters are (place to display shape, the color, dimensions of shape)
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(w-w/15-10, y, 10, 60))
    pygame.draw.ellipse(screen, (255, 255, 255), pygame.Rect(a, b, 10, 10), 0) #draws the ball
    pygame.display.flip() #updates the screen
    screen.fill((0, 0, 0)) #clears the screen before drawing next frame
    clock.tick(60) # sets the frame rate to 60fps