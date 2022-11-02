from pygame.locals import *
import sys
import pygame
import random
import time

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
        self.wall_size=40
        self.xy0state=0    
        self.khit=0
        self.xstate=[0,1,2,3,4,5,6,7,8,9]    
        self.ystate=[0,1,2,3,4,5,6,7,8,9]    
        self.xstate1=0    
        self.ystate1=0    
        self.xstate2=0    
        self.ystate2=0    
        self.ykstate = 0
        self.x=150
        self.y = 30
        self.x1=200
        self.y1 = 50
        self.x2=250
        self.y2 = 80
        self.hit_count=0
        self.stop=0
        self.hit=0
        self.state = 0
        self.kstate = 0

        self.bxt=[0,1,2,3,4,5,6,7,8,9]
        self.byt=[0,1,2,3,4,5,6,7,8,9]
        self.xt=[0,1,2,3,4,5,6,7,8,9]
        self.yt=[0,1,2,3,4,5,6,7,8,9]
    
        for i in range(10):
            self.bxt[i]=300
            self.byt[i]=400
            self.xstate[i]=0
            self.ystate[i]=0
    
    def main(self):
        
        self.game_loop()

        pygame.quit()
        sys.exit()


    def make_target_base(self,i):
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.xt[i], self.yt[i]), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.xt[i]-8, self.yt[i]-8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.xt[i]-8, self.yt[i]+8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.xt[i]+8, self.yt[i]-8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.xt[i]+8, self.yt[i]+8), self.target_size)

    def make_target_base1(self,i):
        pygame.draw.circle(self.main_surface, (255,0,0), (self.xt[i], self.yt[i]), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.xt[i]-8, self.yt[i]-8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.xt[i]-8, self.yt[i]+8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.xt[i]+8, self.yt[i]-8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.xt[i]+8, self.yt[i]+8), self.target_size)

    def make_target_base2(self,i):
        pygame.draw.circle(self.main_surface, (255,255,0), (self.xt[i], self.yt[i]), self.target_size)
        pygame.draw.circle(self.main_surface, (255,255,0), (self.xt[i]-8, self.yt[i]-8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,255,0), (self.xt[i]-8, self.yt[i]+8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,255,0), (self.xt[i]+8, self.yt[i]-8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,255,0), (self.xt[i]+8, self.yt[i]+8), self.target_size)

    def target_move(self,i):
        if(self.xstate[i]==0):
            self.xt[i] += (3+i*2) 
            if(self.xt[i]>400):
                self.xstate[i]=1
        if(self.xstate[i]==1):
              self.xt[i] -= (3+i*2)
              if(self.xt[i]<150):
                self.xstate[i]=0    
        if(self.ystate[i]==0):
            self.yt[i] += (2+i*2)
            if(self.yt[i]>400):
                self.ystate[i]=1
        if(self.ystate[i]==1):
              self.yt[i] -= (2+i*2)
              if(self.yt[i]<100):
                        self.ystate[i]=0    
        

    def game_loop(self):
        pygame.display.set_caption("Dsign")
        clock = pygame.time.Clock()
        stop_button = pygame.Rect(30, 30, 80, 50)  
        start_button = pygame.Rect(30, 130, 80, 50)  
        font = pygame.font.SysFont(None, 25)
        text1 = font.render("STOP", True, (0,0,0))
        text2 = font.render("START", True, (0,0,0))
        start = time.time()
        going = True
        scenario_state=0
        while going:
            t = time.time() - start


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
    
            self.main_surface.fill((220, 220, 220))
            pygame.draw.rect(self.main_surface, (255, 0, 0), stop_button)
            pygame.draw.rect(self.main_surface, (255, 255, 0), start_button)
    
            self.by0 -=10
            self.by1 -=10
            self.by2 -=10
    
            if(self.stop==1):
                pass
            else: 
                #的移動
                for i in range(10):
                    self.target_move(i)	    
            #的 

            if(t>5):
                start = time.time()
                scenario_state += 1
                if(scenario_state == 3):
                    scenario_state =0

            if(scenario_state)==0:
                for i in range(10):
                    self.make_target_base(i)            
                        
            if(scenario_state)==1:
                for i in range(10):
                    self.make_target_base1(i)            

            if(scenario_state)==2:
                for i in range(10):
                    self.make_target_base2(i)            
    
            self.main_surface.blit(text1, (40, 45))
            self.main_surface.blit(text2, (40,145))
            pygame.display.update()
            clock.tick(50)
            
class sub_app(top_app):            
    def target_move(self,i):
        if(self.xstate[i]==0):
            self.xt[i] += (3+i*2) 
            if(self.xt[i]>300):
                self.xstate[i]=1
        if(self.xstate[i]==1):
              self.xt[i] -= (3+i*2)
              if(self.xt[i]<400):
                self.xstate[i]=0    
        if(self.ystate[i]==0):
            self.yt[i] += (2+i*2)
            if(self.yt[i]>100):
                self.ystate[i]=1
        if(self.ystate[i]==1):
              self.yt[i] -= (2+i*2)
              if(self.yt[i]<50):
                        self.ystate[i]=0    
        
      
if __name__ == '__main__':
    sub=sub_app()
    sub.main()