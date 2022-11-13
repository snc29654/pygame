from pygame.locals import *
import sys
import pygame
import random
import time
import tkinter
from tkinter import *
from tkinter import filedialog as tkFileDialog
import os
import glob
filenames =[]


WIDTH  = 1200        # 幅
HEIGHT = 650        # 高さ

WALL_COUNT = 2
BALL_COUNT = 10
TARGET_COUNT = 10

class image_gui():  
    imgs = []
    def __init__(self):  
        self.root = Tk()  
        self.root.title("Image Viewer")  
        self.root.geometry("300x100") 




        button1= Button(self.root, text=u'フォルダー', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=100, y=10) 




        button2 = tkinter.Button(self.root, text = '実行', command=self.quit)
        button2.grid(row=0, column=1)  
        button2.place(x=200, y=10) 



        self.root.mainloop() 

    def check_value(self):

        global interval



        

    def button1_clicked(self):  

        self.check_value()

        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        filenames = []
        filenames = glob.glob('*.jpg')
        print(filenames)


    def button3_clicked(self):  
        global filenames

        self.check_value()



        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        print(filenames)


    def quit(self):
        self.root.destroy()




class top_app():

    def __init__(self):
        pygame.init()
        self.file_no=0
        self.main_surface = pygame.display.set_mode((WIDTH,HEIGHT)) 
        self.img1 = pygame.transform.rotozoom(pygame.image.load(filenames[self.file_no]).convert(), 0, 0.1)
        self.img1 = pygame.transform.rotozoom(self.img1, 0, 0.5)
        self.img2 = pygame.transform.rotozoom(pygame.image.load(filenames[1]).convert(), 0, 0.1)
        self.img2 = pygame.transform.rotozoom(self.img2, 0, 0.5)
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
        self.stop=1
        self.hit=[0,1,2,3,4,5,6,7,8,9]
        self.state = 0
        self.kstate = 0
        self.xstate=[0,1,2,3,4,5,6,7,8,9]
        self.ystate=[0,1,2,3,4,5,6,7,8,9]
        self.x_wall=100
        self.y_wall=100
        self.xwall_state=0
        self.wall_hit = 0
        self.dummy_hit = 0

        self.bxt=[0,1,2,3,4,5,6,7,8,9]
        self.byt=[0,1,2,3,4,5,6,7,8,9]
        self.xk=[0,1,2,3,4,5,6,7,8,9]
        self.yk=[0,1,2,3,4,5,6,7,8,9]
        self.x=[0,1,2,3,4,5,6,7,8,9]
        self.y=[0,1,2,3,4,5,6,7,8,9]
        self.dummy_x=[0,1,2,3,4,5,6,7,8,9]
        self.dummy_y=[0,1,2,3,4,5,6,7,8,9]
        self.xkstate=[0,1,2,3,4,5,6,7,8,9]
        self.ykstate=[0,1,2,3,4,5,6,7,8,9]
        self.scenario_state=0
        self.timeout=0

        self.loop_count=0






        for i in range(BALL_COUNT):
            self.bxt[i]=300
            self.byt[i]=400
            self.xk[i]=150
            self.yk[i]=30
            self.x[i]=150
            self.y[i]=30
            self.dummy_x[i]=150
            self.dummy_y[i]=100
            self.xkstate[i]=0    
            self.ykstate[i]=0    
            self.xstate[i]=0    
            self.ystate[i]=0    
            self.hit[i]=0
            self.dummy_x[i]=self.x_wall
            self.dummy_y[i]=self.y_wall




    def main(self):
        
        self.game_loop()

        pygame.quit()
        sys.exit()

    def hit_check(self):
        for j in range(BALL_COUNT):
            for i in range(TARGET_COUNT):
                if(((self.bxt[j]>(self.x[i]-self.target_size-50))and(self.bxt[j]<(self.x[i]+self.target_size+50)))
                and((self.byt[j]>(self.y[i]-10))and(self.byt[j]<(self.y[i]+10)))):
                    self.hit[i]=1

    def wall_col_check(self):
        for j in range(BALL_COUNT):
            if(((self.bxt[j]>(self.x_wall-self.target_size))and(self.bxt[j]<(self.x_wall+self.target_size+50)))
                and((self.byt[j]>(self.y_wall-10))and(self.byt[j]<(self.y_wall+10)))):
               self.wall_hit = 1

    def dummy_col_check(self):
        for j in range(BALL_COUNT):
            if(((self.dummy_x[j]>(self.x3-50))and(self.dummy_x[j]<(self.x3)))
                and((self.dummy_y[j]>(400-10))and(self.dummy_y[j]<(400+10)))):
               self.dummy_hit = 1

    def all_hit(self):
        for i in range(TARGET_COUNT):
            if (self.hit[i]==0):
                return 0       
            else:
                pass
        return 1

    def make_wall(self):
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+10, self.y_wall-10,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+20, self.y_wall-20,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+20, self.y_wall-10,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall+30, self.y_wall-10,10,10))
        pygame.draw.rect(self.main_surface, (100,0,255), (self.x_wall, self.y_wall,50,10))
        
    def make_target_jpg1(self):
        self.img1 = pygame.transform.rotozoom(pygame.image.load(filenames[self.file_no]).convert(), 0, 0.1)
        self.img1 = pygame.transform.rotozoom(self.img1, 0, 3.0)
        for i in range(TARGET_COUNT):
            if(self.hit[i]==0):
                self.main_surface.blit(self.img1, (self.x[i], self.y[i]))

    def make_target_jpg2(self):
        for i in range(TARGET_COUNT): 
            if(self.hit[i]==0):
                self.main_surface.blit(self.img2, (self.x[i], self.y[i]))

            
                

    def make_dummy(self):
        for i in range(TARGET_COUNT):
            pygame.draw.circle(self.main_surface, (255,0,0), (self.dummy_x[i]+25, self.dummy_y[i]), self.target_size)
            pygame.draw.circle(self.main_surface, (0,0,0), (self.dummy_x[i]+25, self.dummy_y[i]+8), self.target_size)
                

    def make_gun(self):
        pygame.draw.rect(self.main_surface, (255,0,255), (self.x3-10, self.y3-10,20,20))
        pygame.draw.rect(self.main_surface, (255,0,255), (self.x3-25, self.y3,50,20))

    def make_gun_out(self):
        pygame.draw.rect(self.main_surface, (200,200,200), (self.x3-10, self.y3-10,20,20))
        pygame.draw.rect(self.main_surface, (200,200,200), (self.x3-25, self.y3,50,20))

    def make_ball(self):
        for i in range(TARGET_COUNT):
            pygame.draw.circle(self.main_surface, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), (self.bxt[i], self.byt[i]), 10)
    
    
    def target_move(self):
        #的移動
        for i in range(TARGET_COUNT):
            if(self.xstate[i]==0):
                self.x[i] += (1 +i)
                if(self.x[i]>600):
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
                       
    def dummy_move(self):
        for i in range(TARGET_COUNT):

            if(self.xwall_state ==0):
                self.dummy_x[i] += (1+self.scenario_state)
            if(self.xwall_state==1):
                self.dummy_x[i] -= (1+self.scenario_state)

            
            self.dummy_y[i] += (10)
            if(self.dummy_y[i] >400):
                self.dummy_y[i]=100
        
    def wall_move(self):
        if(self.xwall_state ==0):
            self.x_wall += (1+self.scenario_state)
            if(self.x_wall>400):
                self.xwall_state=1
        if(self.xwall_state==1):
            self.x_wall -= (1+self.scenario_state)
            if(self.x_wall<150):
                self.xwall_state=0    



    def game_loop(self):
        pygame.display.set_caption("JPG VIEW ")
        clock = pygame.time.Clock()
        stop_button = pygame.Rect(30, 30, 80, 50)  
        start_button = pygame.Rect(30, 130, 80, 50)  
        reset_button = pygame.Rect(30, 230, 80, 50)  
        font = pygame.font.SysFont(None, 25)
        text1 = font.render("STOP", True, (0,0,0))
        text2 = font.render("START", True, (0,0,0))
        text3 = font.render(" ", True, (0,0,0))
        text4 = font.render(" ", True, (0,0,0))
        texthit = font.render("  ", True, (0,0,0))
        start = time.time()
        
        going = True
        while going:
            if (self.stop==1):
                start = time.time()
                
            t = time.time() - start
            if(t>300):
                self.timeout=1

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
                        #弾発射
                        self.file_no += 1

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
                        #弾発射
                        self.bxt[self.xy0state]=self.x3
                        self.byt[self.xy0state]=400
                        self.xy0state += 1
                        if(self.xy0state==9):
                            self.xy0state=0    
                        self.stop=0
    
            #的衝突 
            self.hit_check()            
            #self.wall_col_check()    
            self.dummy_col_check()      
    
            self.main_surface.fill((220, 220, 220))
            pygame.draw.rect(self.main_surface, (255, 0, 0), stop_button)
            pygame.draw.rect(self.main_surface, (255, 255, 0), start_button)
            # pygame.draw.rect(self.main_surface, (0, 0, 255), reset_button)
    
            self.by0 -=10
            self.by1 -=10
            self.by2 -=10
    
            if(self.stop==1):
                pass
            else: 
                for i in range(BALL_COUNT):
                    self.byt[i]-=10
    
                #的移動
                self.target_move()	    
    
                #self.make_wall()     
                #self.wall_move()     
                
                #弾             
                #self.make_ball()
                
                #大砲             
                #self.make_gun()
                #self.make_dummy()
                #self.dummy_move()
    
                        
                        
            #的 

            if(self.scenario_state==0):            
                texthit = font.render(" ", True, (0,0,0))
                self.make_target_jpg1()
                if (self.all_hit()==1):
                    self.file_no += 1
                    for i in range(BALL_COUNT):
                       self.hit[i]=0
                    
            if(self.scenario_state==1):            
                texthit = font.render(" ", True, (0,0,0))
                self.make_target_jpg2()
                if (self.all_hit()==1):
                    self.scenario_state = 2
                    for i in range(BALL_COUNT):
                           self.hit[i]=0
            if(self.scenario_state==2):            
                texthit = font.render(" ", True, (0,0,0))
                self.stop=1                            
            
            
            
                
            self.main_surface.blit(text1, (40, 45))
            self.main_surface.blit(text2, (40,145))
            #self.main_surface.blit(text3, (40,245))
            #self.main_surface.blit(text4, (40,430))
            if(self.dummy_hit==1):        
                self.make_gun_out()
                texthit = font.render(" ", True, (255,0,0))
                self.stop=0                    
            if(self.wall_hit==1):        
                texthit = font.render(" ", True, (255,0,0))
                self.stop=0                    
            
            if(self.timeout==1):        
                texthit = font.render("TIMEOUT!", True, (255,0,0))
                self.stop=1                    
            if(self.khit==1):        
                texthit = font.render("game over count="+str(self.hit_count), True, (0,0,0))
            else:
                pass
            self.main_surface.blit(texthit, (200,45))
            pygame.display.update()
            clock.tick(50)
            self.loop_count+=1
if __name__ == '__main__':
    image_gui()  
    app = top_app()
    app.main()