


import pygame
import random
pygame.init()


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Tetris")



RandomX = int(random.randint(0,100))
RandomY= int(random.randint(0,100))
RandomH = int(random.randint(0,200))
RandomW = int(random.randint(0,200))

x = 40
y = 20
vel = 5

hight = int(RandomH)
width = int(RandomW)

left = False
right = False
walkC = 0

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left= True
        right = False
    if keys[pygame.K_RIGHT] and x < 500 - width:
       x += vel
       right = True
       left = False

# borderless
    if keys[pygame.K_UP]:
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - hight - vel:
        y += vel
    if keys[pygame.K_r]:
        pass

    # if keys[pygame.K_SPACE]:
    #pygame.draw.rect(screen, (255, 0, 0), (x, y, width, hight))

    screen.fill((0,0,0))
    RandomC = random.choice(pygame.draw.rect(screen, (255, 0, 0), (x, y, hight,width)))
    pygame.display.update()
pygame.quit()
