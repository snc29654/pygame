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
        self.wall_size=40
        self.xy0state=0    
        self.khit=0
        self.xstate=0    
        self.ystate=0    
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
    
        for i in range(10):
            self.bxt[i]=300
            self.byt[i]=400

    
    def main(self):
        
        self.game_loop()

        pygame.quit()
        sys.exit()



    
    def make_target(self):
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x, self.y), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x-8, self.y-8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x-8, self.y+8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x+8, self.y-8), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x+8, self.y+8), self.target_size)

    def make_target_out(self):
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x, self.y), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x-20, self.y-20), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x-20, self.y+20), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x+20, self.y-20), self.target_size)
        pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.x+20, self.y+20), self.target_size)


    def make_target_base(self):
        pygame.draw.circle(self.main_surface, (255,255,0), (self.x, self.y), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.x-8, self.y-8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.x-8, self.y+8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.x+8, self.y-8), self.target_size)
        pygame.draw.circle(self.main_surface, (255,0,0), (self.x+8, self.y+8), self.target_size)

    def make_target_base1(self):
        pygame.draw.circle(self.main_surface, (255,0,255), (self.x1, self.y1), self.target_size)
        pygame.draw.circle(self.main_surface, (100,255,0), (self.x1-8, self.y1-8), self.target_size)
        pygame.draw.circle(self.main_surface, (100,255,0), (self.x1-8, self.y1+8), self.target_size)
        pygame.draw.circle(self.main_surface, (100,255,0), (self.x1+8, self.y1-8), self.target_size)
        pygame.draw.circle(self.main_surface, (100,255,0), (self.x1+8, self.y1+8), self.target_size)

    def make_target_base2(self):
        pygame.draw.circle(self.main_surface, (255,0,255), (self.x2, self.y2), self.target_size)
        pygame.draw.circle(self.main_surface, (0,100,100), (self.x2-8, self.y2-8), self.target_size)
        pygame.draw.circle(self.main_surface, (0,100,100), (self.x2-8, self.y2+8), self.target_size)
        pygame.draw.circle(self.main_surface, (0,100,100), (self.x2+8, self.y2-8), self.target_size)
        pygame.draw.circle(self.main_surface, (0,100,100), (self.x2+8, self.y2+8), self.target_size)


    def target_move(self):
        #的移動
        if(self.xstate==0):
            self.x += (3 +self.hit_count)
            if(self.x>400):
                self.xstate=1
        if(self.xstate==1):
              self.x -= (3 +self.hit_count)
              if(self.x<150):
                self.xstate=0    


        #的移動
        if(self.ystate==0):
            self.y += (2 +self.hit_count)
            if(self.y>300):
                self.ystate=1
        if(self.ystate==1):
              self.y -= (2 +self.hit_count)
              if(self.y<150):
                        self.ystate=0    
        

    def target_move1(self):
        #的移動
        if(self.xstate1==0):
            self.x1 += (5 +self.hit_count)
            if(self.x1>400):
                self.xstate1=1
        if(self.xstate1==1):
              self.x1 -= (5 +self.hit_count)
              if(self.x1<150):
                self.xstate1=0    


        #的移動
        if(self.ystate1==0):
            self.y1 += (5 +self.hit_count)
            if(self.y1>300):
                self.ystate1=1
        if(self.ystate1==1):
              self.y1 -= (5 +self.hit_count)
              if(self.y1<150):
                        self.ystate1=0    
        
    def target_move2(self):
        #的移動
        if(self.xstate2==0):
            self.x2 += (8 +self.hit_count)
            if(self.x2>400):
                self.xstate2=1
        if(self.xstate2==1):
              self.x2 -= (8 +self.hit_count)
              if(self.x2<150):
                self.xstate2=0    


        #的移動
        if(self.ystate2==0):
            self.y2 += (8 +self.hit_count)
            if(self.y2>300):
                self.ystate2=1
        if(self.ystate2==1):
              self.y2 -= (8 +self.hit_count)
              if(self.y2<150):
                        self.ystate2=0    


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
        pygame.display.set_caption("Dsign")
        clock = pygame.time.Clock()
        stop_button = pygame.Rect(30, 30, 80, 50)  
        start_button = pygame.Rect(30, 130, 80, 50)  
        #reset_button = pygame.Rect(30, 230, 80, 50)  
        font = pygame.font.SysFont(None, 25)
        text1 = font.render("STOP", True, (0,0,0))
        text2 = font.render("START", True, (0,0,0))
        #text3 = font.render("SHOOT", True, (0,0,0))
        #text4 = font.render("CURSOL:SHOOTER MOVE /  SPACE ball start   ", True, (0,0,0))
        
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
    
                
    
    
    
    
            self.main_surface.fill((220, 220, 220))
            pygame.draw.rect(self.main_surface, (255, 0, 0), stop_button)
            pygame.draw.rect(self.main_surface, (255, 255, 0), start_button)
    
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
                self.target_move1()	    
                self.target_move2()	    
    
                #障壁移動
                self.wall_move()	    
    
                        
                        
            #的 
            self.make_target_base()            
            self.make_target_base1()            
            self.make_target_base2()            
    
            self.main_surface.blit(text1, (40, 45))
            self.main_surface.blit(text2, (40,145))
            #self.main_surface.blit(text3, (40,245))
            #self.main_surface.blit(text4, (40,430))
            pygame.display.update()
            clock.tick(50)
if __name__ == '__main__':
    app = top_app()
    app.main()