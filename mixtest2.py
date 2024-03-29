from pygame.locals import *
import sys
import pygame

WIDTH  = 640        # 幅
HEIGHT = 400        # 高さ


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
    text4 = font.render("CURSOL:SHOOTER MOVE /  SPACE ball start   ", True, (0,0,0))
    texthit = font.render("HIT!", True, (0,0,0))
    x=150
    xk=150
    yk=200
    y = 30
    x2=300
    by0 =400
    by1 =400
    by2 =400
    target_size=20
    x3=300
    bx30=300
    bx31=300
    bx32=300
    y3 =400
    xystate=0    
    khit=0
    ystate=0    
    
    bxt=[0,1,2,3,4,5,6,7,8,9]
    byt=[0,1,2,3,4,5,6,7,8,9]

    for i in range(10):
        bxt[i]=300
        byt[i]=400


    hit_count=0
    stop=0
    hit=0
    going = True
    state = 0
    kstate = 0
    ykstate = 0
    bstate = 0
    while going:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            #大砲移動　左
            x3=x3-10        
        if pressed[pygame.K_RIGHT]:
            #大砲移動　右
            x3=x3+10        


        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                going = False


            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                   #大砲移動　左
                    x3=x3-10        
                if event.key == K_RIGHT:
                   #大砲移動　右
                    x3=x3+10        
                if event.key == K_SPACE:
                    #玉発射
                    bxt[xystate]=x3
                    byt[xystate]=400
                    xystate += 1
                    if(xystate==9):
                        xystate=0    
                    stop=0


            if event.type == pygame.MOUSEBUTTONDOWN:
                if stop_button.collidepoint(event.pos):
                    stop=1
                if start_button.collidepoint(event.pos):
                    stop=0
                if reset_button.collidepoint(event.pos):
                    #玉発射
                    bxt[xystate]=x3
                    byt[xystate]=400
                    xystate += 1
                    if(xystate==9):
                        xystate=0    
                    stop=0

        #的衝突             
        for i in range(10):
            if(((bxt[i]>(x-target_size))and(bxt[i]<(x+target_size)))
             and((byt[i]>(y-10))and(byt[i]<(y+10)))):
                hit=1

        #障壁衝突             
        for i in range(10):
            if(((bxt[i]>(xk))and(bxt[i]<(xk+target_size+40)))
             and((byt[i]>(yk))and(byt[i]<(yk+target_size)))):
                stop=1
                khit=1
            




        main_surface.fill((220, 220, 220))
        pygame.draw.rect(main_surface, (255, 0, 0), stop_button)
        pygame.draw.rect(main_surface, (255, 255, 0), start_button)
        pygame.draw.rect(main_surface, (0, 0, 255), reset_button)

        by0 -=10
        by1 -=10
        by2 -=10

        if(stop==1):
            pass
        else: 
            for i in range(10):
                byt[i]-=10

            #的移動
            if(state==0):
                x += 3
                if(x>400):
                    state=1
            if(state==1):
                  x -= 3
                  if(x<150):
                    state=0    


            #的移動
            if(ystate==0):
                y += 2
                if(y>300):
                    ystate=1
            if(ystate==1):
                  y -= 2
                  if(y<150):
                    ystate=0    


            #障壁移動
            if(kstate==0):
                xk += 2
                if(xk>400):
                    kstate=1
            if(kstate==1):
                  xk -= 2
                  if(xk<150):
                    kstate=0    

            if(ykstate==0):
                yk += 2
                if(yk>300):
                    ykstate=1
            if(ykstate==1):
                  yk -= 2
                  if(yk<150):
                    ykstate=0    

                    
                    
        #的             
        pygame.draw.circle(main_surface, (0,0,255), (x, y), target_size)

        #障壁             
        pygame.draw.rect(main_surface, (100,0,255), (xk, yk,50,20))

        #玉             
        for i in range(10):
            pygame.draw.circle(main_surface, (0,0,0), (bxt[i], byt[i]), 10)
            
        #大砲             
        pygame.draw.rect(main_surface, (255,0,255), (x3-25, y3,50,20))



        main_surface.blit(text1, (40, 45))
        main_surface.blit(text2, (40,145))
        main_surface.blit(text3, (40,245))
        main_surface.blit(text4, (40,430))
        if(hit==1):
            hit_count+=1
            hit=0
            target_size-=1
            if(target_size<10):
                target_size=20
        if(khit==1):        
            texthit = font.render("game over count="+str(hit_count), True, (0,0,0))
        else:
            texthit = font.render("hit count="+str(hit_count), True, (0,0,0))
        main_surface.blit(texthit, (200,45))
        pygame.display.update()
        clock.tick(50)
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()