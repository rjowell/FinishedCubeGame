import pygame, sys, time, random
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Cuber.io Game")

cubeSize = 20

#RGB Colors
yellow = (255,255, 0)
white = (255,255,255)
myColor = (255,0,0)
randomColor = (45, 252, 222);
bigColor = (0,100,200);

food = [random.randrange(1,500),random.randrange(1,500), 10, 10]
Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]


speed = 5

cubeX = 250
cubeY = 250
cubeSize = 20

run = True
while run:
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(10)
    win.fill(white)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        if cubeX >= 480:
            cubeX = 480
        else:
            cubeX += speed

    if keys[pygame.K_LEFT]:
        if cubeX <= 0:
            cubeX = 0
        else:
            cubeX -= speed

    if keys[pygame.K_UP]:
        if cubeY <= 0:
            cubeY = 0
        else:
            cubeY -= speed

    if keys[pygame.K_DOWN]:
        if cubeY >= 480:
            cubeY = 480
        else:
            cubeY += speed
    
    cube = pygame.Rect(cubeX,cubeY,cubeSize,cubeSize)

    #draw rectangle
    if cubeSize <= 100:
        pygame.draw.rect(win, myColor, cube)
    else:
        pygame.draw.rect(win, bigColor, cube)

    #pygame.display.update()

    food_status = True
    Bfood_status = True

    #Check Collision With Food
    if cube.colliderect(food):
        cubeSize += 10
        food_status = False

    #Check Collision With Bad Food
    if cube.colliderect(Bfood):
        cubeSize -= 10
        Bfood_status = False

    # Spawn new food
    if food_status == False:
        food = [random.randrange(1,500),random.randrange(1,500), 10, 10]

    # Spawn new Bad food
    if Bfood_status == False:
        Bfood = [random.randrange(1,500),random.randrange(1,500), 10, 10]

    # draw food
    pygame.draw.rect(win, randomColor, pygame.Rect(food))

    # draw Bad food
    pygame.draw.rect(win, yellow, pygame.Rect(Bfood))
    
    pygame.display.update()

#pygame.quit()
