#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from typing import Tuple

WIN_HEIGHT, WIN_WIDTH = 500, 500

def main():
    import pygame
    import random

    pygame.init()


    screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption("Tetris")


    red = (255, 0, 0)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    white = (255, 255, 255)
    colors = red, black, red, green, blue, white
    cor_peca = random.choice(colors)


    RandomX = int(random.randint(0,100))
    RandomY= int(random.randint(0,100))
    RandomH = int(random.randint(0,200))
    RandomW = int(random.randint(0,200))

    x = 200
    y = 4
    vel = 5

    height = 30
    width = 30

    left = True
    right = True
    down = True
    up = True


    run = True
    while run:
        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        #print(f"K_LEFT={pygame.K_LEFT},K_RIGHT={pygame.K_RIGHT}, K_DOWN={pygame.K_DOWN}, K_UP={pygame.K_UP}")


        if keys[pygame.K_LEFT] and x > vel:
            if left == False:
                 print("limite")

            if left == True:
                x -= vel
                print("LEFT",x)
                if x < 5:
                   x_abosolute = x - 5
                   x = x - x_abosolute

        if keys[pygame.K_RIGHT] and x < 500 -width:
            if right  == False:
                 print('limite')

            if right == True:
                x += vel

                if x > 500:
                   x_abosolute1 = x - 500
                   x =  x - x_abosolute1

                print("RIGHT:",x)


        if keys[pygame.K_UP]:
            if up  == False:
                 print("limite")

            if up == True:
                y -= vel
                print("UP:",y)


        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            if down == True:
                y += vel
                print("DOWN:",y )  #"vel= ", vel)

            if down == False:
                print("limite ")

        if keys[pygame.K_r]:
            exit()

        screen.fill((0,0,0))


        RandomC = random.choice(pygame.draw.rect(screen, cor_peca, (x, y, height, width)))
        pygame.display.flip()
    pygame.quit()
def eh_possivel_mover_peca() -> bool:
    if keys[pygame.K_LEFT] and x < 0:
        return left == False
    if keys[pygame.K_RIGHT] and x > 500:
        return right == false
    if keys[pygame.K_UP] and y < 0:
        return up == False
    if keys[pygame.K_DOWN] and y > 500:
        return down == False


def mover_peca(key_pressed, x, y, width, height) -> Tuple[int,int]:
    global WIN_HEIGHT, WIN_WIDTH
    new_x = x
    new_y = y
    # TODO: implementar a logica que permite/ou não, mover a peca :)
    return new_x, new_y

# só executará o tetris quando chamado diretamente,
# não quando "import tetris"
if __name__ == "__main__":
    main()
