import pygame
from pygame.locals import *
import sys
import time
import threading
class game_main():
    def main(self):
        pygame.init() # 初期化
        (self.w, self.h) = (500, 637)
        (self.x, self.y) = (self.w/2, self.h/2)
        (self.w2, self.h2) = (500, 637)
        (self.x2, self.y2) = (self.w2/2, self.h2/2)
        pygame.display.set_mode((self.w, self.h), 0, 32)
        self.screen = pygame.display.get_surface()
        self.screen2 = pygame.display.get_surface()
        pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定
        self.bg = pygame.image.load("back.jpg").convert_alpha() # 背景画像の指定
        self.rect_bg = self.bg.get_rect() # 画像のサイズ取得？？だと思われる
        self.player = pygame.image.load("char.jpg").convert_alpha() # キャラ画像の指定
        self.player2 = pygame.image.load("char2.jpg").convert_alpha() # キャラ画像の指定
        self.rect_player = self.player.get_rect() # 謎
        self.rect_player.center = (self.x, self.y) # キャラ座標
        self.rect_player2 = self.player2.get_rect() # 謎
        self.rect_player2.center = (self.x2, self.y2) # キャラ座標
        self.x=100
        self.y=100
        self.state=0
        self.x2=100
        self.y2=100
        self.state2=0
    def start_test(self):
        while(True):
            self.screen.fill((0, 0, 0, 0)) # 背景色の指定。RGBのはず
            self.screen.blit(self.bg, self.rect_bg) # 背景画像の描画
            self.screen.blit(self.player, self.rect_player) # キャラの描画
            self.screen2.blit(self.player2, self.rect_player2) # キャラの描画
            #pygame.time.wait(1) # 更新間隔。多分ミリ秒
            pygame.display.update() # 画面更新
            if(self.state==0):
                self.x += 1 
                if(self.x==400):
                    self.state=1
            elif(self.state==1):
                self.y += 1 
                if(self.y==400):
                    self.state=2
            elif(self.state==2):
                self.x -= 1 
                if(self.x==100):
                    self.state=3
            else:
                self.y -= 1 
                if(self.y==100):
                    self.state=0
            if(self.state2==0):
                self.x2 += 1 
                if(self.x2==200):
                    self.state2=1
            elif(self.state2==1):
                self.y2 += 1 
                if(self.y2==200):
                    self.state2=2
            elif(self.state2==2):
                self.x2 -= 1 
                if(self.x2==50):
                    self.state2=3
            else:
                self.y2 -= 1 
                if(self.y2==50):
                    self.state2=0
            self.rect_player.center = (self.x, self.y)
            self.rect_player2.center = (self.x2, self.y2)
            if self.x > self.w: # 端まで来たら座標を0にリセット
                self.x = 0
            if self.y > self.h: # 同上
                self.y = 0
            for event in pygame.event.get(): # 終了処理
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
if __name__ == "__main__":
    
    g=game_main()     
    g.main()
    thread1 = threading.Thread(target=g.start_test) 
    thread1.start()