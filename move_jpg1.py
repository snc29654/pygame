# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
import time
def main():
    pygame.init() # 初期化
    (w, h) = (500, 637)
    (x, y) = (w/2, h/2)
    pygame.display.set_mode((w, h), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("Pygame Test") # ウィンドウの上の方に出てくるアレの指定
    bg = pygame.image.load("back.jpg").convert_alpha() # 背景画像の指定
    rect_bg = bg.get_rect() # 画像のサイズ取得？？だと思われる
    player = pygame.image.load("char.jpg").convert_alpha() # キャラ画像の指定
    rect_player = player.get_rect() # 謎
    rect_player.center = (x, y) # キャラ座標
    x=100
    y=100
    state=0
    while(True):
        screen.fill((0, 0, 0, 0)) # 背景色の指定。RGBのはず
        screen.blit(bg, rect_bg) # 背景画像の描画
        screen.blit(player, rect_player) # キャラの描画
        #pygame.time.wait(1) # 更新間隔。多分ミリ秒
        pygame.display.update() # 画面更新
        if(state==0):
            x += 1 
            if(x==400):
                state=1
        elif(state==1):
            y += 1 
            if(y==400):
                state=2
        elif(state==2):
            x -= 1 
            if(x==100):
                state=3
        else:
            y -= 1 
            if(y==100):
                state=0
        rect_player.center = (x, y)
        if x > w: # 端まで来たら座標を0にリセット
            x = 0
        if y > h: # 同上
            y = 0
        for event in pygame.event.get(): # 終了処理
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
if __name__ == "__main__":
    main()
