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



    RandomX = int(random.randint(0,100))
    RandomY= int(random.randint(0,100))
    RandomH = int(random.randint(0,200))
    RandomW = int(random.randint(0,200))

    x = 40
    y = 20
    vel = 5

    height = int(RandomH)
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

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_r]:
            pass

        # if keys[pygame.K_SPACE]:
        #pygame.draw.rect(screen, (255, 0, 0), (x, y, width, hight))

        screen.fill((0,0,0))
        cor_peca = (255, 0, 0)
        RandomC = random.choice(pygame.draw.rect(screen, cor_peca, (x, y, height, width)))
        pygame.display.update()
    pygame.quit()

def eh_possivel_mover_peca() -> bool:
    # TODO
    return True

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