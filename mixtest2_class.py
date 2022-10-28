from pygame.locals import *
import sys
import pygame
import random


WIDTH  = 640        # 幅
HEIGHT = 400        # 高さ

class top_app():

    def __init__(self):
        pygame.init()
        self.main_surface = pygame.display.set_mode((500, 500)) 
        self.xk=150
        self.yk=200
        self.by0 =400
        self.by1 =400
        self.by2 =400
        self.x3=300
        self.y3 =400
        self.target_size=8
        self.xy0state=0    
        self.khit=0
        self.ystate=0    
        self.ykstate = 0
        self.x=150
        self.y = 30
        self.hit_count=0
        self.stop=0
        self.hit=0
        self.state = 0
        self.kstate = 0

        self.bxt=[0,1,2,3,4,5,6,7,8,9]
        self.byt=[0,1,2,3,4,5,6,7,8,9]
    
        for i in range(10):
            self.bxt[i]=300
            self.byt[i]=400

    
    def main(self):
        
        self.game_loop()

        pygame.quit()
        sys.exit()

    def hit_check(self):
        for i in range(10):
            if(((self.bxt[i]>(self.x-self.target_size))and(self.bxt[i]<(self.x+self.target_size)))
             and((self.byt[i]>(self.y-7))and(self.byt[i]<(self.y+7)))):
                self.hit=1


    def wall_out(self):
        for i in range(10):
            if(((self.bxt[i]>(self.xk))and(self.bxt[i]<(self.xk+self.target_size+40)))
             and((self.byt[i]>(self.yk))and(self.byt[i]<(self.yk+self.target_size)))):
                self.stop=1
                self.khit=1
    
    def make_target(self):
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x, self.y), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x-8, self.y-8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x-8, self.y+8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x+8, self.y-8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x+8, self.y+8), self.target_size)

    def target_move(self):
        #的移動
        if(self.state==0):
            self.x += (3 +self.hit_count)
            if(self.x>400):
                self.state=1
        if(self.state==1):
              self.x -= (3 +self.hit_count)
              if(self.x<150):
                self.state=0    


        #的移動
        if(self.ystate==0):
            self.y += (2 +self.hit_count)
            if(self.y>300):
                self.ystate=1
        if(self.ystate==1):
              self.y -= (2 +self.hit_count)
              if(self.y<150):
                        self.ystate=0    
        

    def wall_move(self):
        if(self.kstate==0):
            self.xk += 2
            if(self.xk>400):
                self.kstate=1
        if(self.kstate==1):
              self.xk -= 2
              if(self.xk<150):
                self.kstate=0    

        if(self.ykstate==0):
            self.yk += 2
            if(self.yk>300):
                self.ykstate=1
        if(self.ykstate==1):
              self.yk -= 2
              if(self.yk<150):
                self.ykstate=0    


    def game_loop(self):
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
        
        going = True
        while going:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                #大砲移動　左
                self.x3=self.x3-10        
            if pressed[pygame.K_RIGHT]:
                #大砲移動　右
                self.x3=self.x3+10        
    
    
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    going = False
    
    
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                       #大砲移動　左
                        self.x3=self.x3-10        
                    if event.key == K_RIGHT:
                       #大砲移動　右
                        self.x3=self.x3+10        
                    if event.key == K_SPACE:
                        #玉発射
                        self.bxt[self.xy0state]=self.x3
                        self.byt[self.xy0state]=400
                        self.xy0state += 1
                        if(self.xy0state==9):
                            self.xy0state=0    
                        self.stop=0
    
    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if stop_button.collidepoint(event.pos):
                        self.stop=1
                    if start_button.collidepoint(event.pos):
                        self.stop=0
                    if reset_button.collidepoint(event.pos):
                        #玉発射
                        self.bxt[self.xy0state]=self.x3
                        self.byt[self.xy0state]=400
                        self.xy0state += 1
                        if(self.xy0state==9):
                            self.xy0state=0    
                        self.stop=0
    
            #的衝突 
            self.hit_check()            
    
            #障壁衝突 
            self.wall_out()            
                
    
    
    
    
            self.main_surface.fill((220, 220, 220))
            pygame.draw.rect(self.main_surface, (255, 0, 0), stop_button)
            pygame.draw.rect(self.main_surface, (255, 255, 0), start_button)
            pygame.draw.rect(self.main_surface, (0, 0, 255), reset_button)
    
            self.by0 -=10
            self.by1 -=10
            self.by2 -=10
    
            if(self.stop==1):
                pass
            else: 
                for i in range(10):
                    self.byt[i]-=10
    
                #的移動
                self.target_move()	    
    
                #障壁移動
                self.wall_move()	    
    
                        
                        
            #的 
            self.make_target()            
    
            #障壁             
            pygame.draw.rect(self.main_surface, (100,0,255), (self.xk, self.yk,50,20))
    
            #玉             
            for i in range(10):
                pygame.draw.circle(self.main_surface, (0,0,0), (self.bxt[i], self.byt[i]), 10)
                
            #大砲             
            pygame.draw.rect(self.main_surface, (255,0,255), (self.x3-25, self.y3,50,20))
    
    
    
            self.main_surface.blit(text1, (40, 45))
            self.main_surface.blit(text2, (40,145))
            self.main_surface.blit(text3, (40,245))
            self.main_surface.blit(text4, (40,430))
            if(self.hit==1):
                self.hit_count+=1
                self.hit=0
                self.target_size-=1
                if(self.target_size<10):
                    self.target_size=8
            if(self.khit==1):        
                texthit = font.render("game over count="+str(self.hit_count), True, (0,0,0))
            else:
                texthit = font.render("hit count="+str(self.hit_count), True, (0,0,0))
            self.main_surface.blit(texthit, (200,45))
            pygame.display.update()
            clock.tick(50)
if __name__ == '__main__':
    app = top_app()
    app.main()