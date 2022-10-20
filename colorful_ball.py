from pygame.locals import *
import sys
import pygame

import random

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((500, 500)) 
    pygame.display.set_caption("BALL STOP START")
    clock = pygame.time.Clock()
    stop_button = pygame.Rect(30, 30, 80, 50)  
    start_button = pygame.Rect(30, 130, 80, 50)  
    font = pygame.font.SysFont(None, 25)
    text1 = font.render("STOP", True, (0,0,0))
    text2 = font.render("START", True, (0,0,0))
    
    y = 0
    stop=0
    going = True
    while going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stop_button.collidepoint(event.pos):
                    stop=1
                if start_button.collidepoint(event.pos):
                    stop=0
        main_surface.fill((220, 220, 220))
        pygame.draw.rect(main_surface, (255, 0, 0), stop_button)
        pygame.draw.rect(main_surface, (255, 255, 0), start_button)
        if(stop==1):
            pass
        else:    
            y = random.randint(50, 400)
            x = random.randint(150, 400)
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            s = random.randint(10, 80)

        pygame.draw.circle(main_surface, (r,g,b), (x, y), s)
        main_surface.blit(text1, (40, 45))
        main_surface.blit(text2, (40,145))
        pygame.display.update()
        clock.tick(10)
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()