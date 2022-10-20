from pygame.locals import *
import sys
import pygame
def main():
    pygame.init()
    main_surface = pygame.display.set_mode((500, 500)) 
    pygame.display.set_caption("SHOOTING TEST")
    clock = pygame.time.Clock()
    stop_button = pygame.Rect(30, 30, 80, 50)  
    start_button = pygame.Rect(30, 130, 80, 50)  
    reset_button = pygame.Rect(30, 230, 80, 50)  
    font = pygame.font.SysFont(None, 25)
    text1 = font.render("STOP", True, (0,0,0))
    text2 = font.render("START", True, (0,0,0))
    text3 = font.render("SHOOT", True, (0,0,0))
    texthit = font.render("HIT!", True, (0,0,0))
    x=150
    y = 30
    x2=300
    y2 =400
    stop=0
    hit=0
    going = True
    state = 0
    while going:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                going = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if stop_button.collidepoint(event.pos):
                    stop=1
                if start_button.collidepoint(event.pos):
                    stop=0
                if reset_button.collidepoint(event.pos):
                    y2=400
                    stop=0

        if(((x2>(x-10))and(x2<(x+10)))
         and((y2>(y-10))and(y2<(y+10)))):
            print("hit")
            hit=1


        main_surface.fill((220, 220, 220))
        pygame.draw.rect(main_surface, (255, 0, 0), stop_button)
        pygame.draw.rect(main_surface, (255, 255, 0), start_button)
        pygame.draw.rect(main_surface, (0, 0, 255), reset_button)
        y2 -=10
        if(stop==1):
            pass
        else: 
            if(state==0):
                x += 3
                if(x>400):
                    state=1
            if(state==1):
                x -= 3
                if(x<150):
                    state=0    
                    
        pygame.draw.circle(main_surface, (0,0,255), (x, y), 20)
        pygame.draw.circle(main_surface, (255,0,255), (x2, y2), 20)
        main_surface.blit(text1, (40, 45))
        main_surface.blit(text2, (40,145))
        main_surface.blit(text3, (40,245))
        if(hit==1):
            main_surface.blit(texthit, (200,45))
            stop=1
        pygame.display.update()
        clock.tick(50)
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()