from pygame.locals import *
import sys
import pygame
import random


WIDTH  = 640        # 幅
HEIGHT = 400        # 高さ

WALL_COUNT = 2
TARGET_COUNT = 6

class top_app():

    def __init__(self):
        pygame.init()
        self.main_surface = pygame.display.set_mode((500, 500)) 
        self.by0 =400
        self.by1 =400
        self.by2 =400
        self.x3=300
        self.y3 =400
        self.target_size=8
        self.wall_size=40
        self.xy0state=0    
        self.khit=0
        self.state = 0
        self.hit_count=0
        self.stop=0
        self.hit=[0,1,2,3,4,5,6,7,8,9]
        self.state = 0
        self.kstate = 0
        self.xstate=[0,1,2,3,4,5,6,7,8,9]
        self.ystate=[0,1,2,3,4,5,6,7,8,9]

        self.bxt=[0,1,2,3,4,5,6,7,8,9]
        self.byt=[0,1,2,3,4,5,6,7,8,9]
        self.xk=[0,1,2,3,4,5,6,7,8,9]
        self.yk=[0,1,2,3,4,5,6,7,8,9]
        self.x=[0,1,2,3,4,5,6,7,8,9]
        self.y=[0,1,2,3,4,5,6,7,8,9]
        self.xkstate=[0,1,2,3,4,5,6,7,8,9]
        self.ykstate=[0,1,2,3,4,5,6,7,8,9]
    
        for i in range(10):
            self.bxt[i]=300
            self.byt[i]=400
            self.xk[i]=150
            self.yk[i]=30
            self.x[i]=150
            self.y[i]=30
            self.xkstate[i]=0    
            self.ykstate[i]=0    
            self.xstate[i]=0    
            self.ystate[i]=0    
            self.hit[i]=0
    def main(self):
        
        self.game_loop()

        pygame.quit()
        sys.exit()

    def hit_check(self):
        for j in range(10):
            for i in range(TARGET_COUNT):
                if(((self.bxt[j]>(self.x[i]-self.target_size-10))and(self.bxt[j]<(self.x[i]+self.target_size+10)))
                and((self.byt[j]>(self.y[i]-10))and(self.byt[j]<(self.y[i]+10)))):
                    self.hit[i]=1

    def all_hit(self):
        for i in range(TARGET_COUNT):
            if (self.hit[i]==0):
                return 0       
            else:
                pass
        return 1
            
    def make_target(self):
        for i in range(TARGET_COUNT):
            if(self.hit[i]==0):
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i], self.y[i]), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]-8, self.y[i]-8), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]-8, self.y[i]+8), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]+8, self.y[i]-8), self.target_size)
                pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x[i]+8, self.y[i]+8), self.target_size)
                pygame.draw.circle(self.main_surface, (0,0,0), (self.x[i], self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]+8, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]-8, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]+16, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]-16, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]+24, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,255,0), (self.x[i]-24, self.y[i]+16), self.target_size)
                pygame.draw.circle(self.main_surface, (0,0,0), (self.x[i], self.y[i]+24), self.target_size)
                pygame.draw.circle(self.main_surface, (0,0,0), (self.x[i], self.y[i]+32), self.target_size)
            else:
                pass
                



    def make_taiho(self):
        pygame.draw.rect(self.main_surface, (255,0,255), (self.x3-10, self.y3-10,20,20))
        pygame.draw.rect(self.main_surface, (255,0,255), (self.x3-25, self.y3,50,20))

    def make_tama(self):
        for i in range(TARGET_COUNT):
            pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.bxt[i], self.byt[i]), 10)
    
    
    def target_move(self):
        #的移動
        for i in range(TARGET_COUNT):
            if(self.xstate[i]==0):
                self.x[i] += (1 +i)
                if(self.x[i]>400):
                    self.xstate[i]=1
            if(self.xstate[i]==1):
                self.x[i] -= (1 +i)
                if(self.x[i]<150):
                    self.xstate[i]=0    


            if(self.ystate[i]==0):
                self.y[i] += (1 +i)
                if(self.y[i]>300):
                    self.ystate[i]=1
            if(self.ystate[i]==1):
                self.y[i] -= (1 +i)
                if(self.y[i]<150):
                    self.ystate[i]=0    
        


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
        texthit = font.render("  ", True, (0,0,0))
        
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
    
    
                        
                        
            #的 
            self.make_target()            
                    
                
                
            #玉             
            self.make_tama()
                
            #大砲             
            self.make_taiho()
    
    
            self.main_surface.blit(text1, (40, 45))
            self.main_surface.blit(text2, (40,145))
            self.main_surface.blit(text3, (40,245))
            self.main_surface.blit(text4, (40,430))
            if (self.all_hit()==1):
                texthit = font.render("GAME CLEAR !", True, (0,0,0))
                    
            if(self.khit==1):        
                texthit = font.render("game over count="+str(self.hit_count), True, (0,0,0))
            else:
                pass
            self.main_surface.blit(texthit, (200,45))
            pygame.display.update()
            clock.tick(50)
if __name__ == '__main__':
    app = top_app()
    app.main()