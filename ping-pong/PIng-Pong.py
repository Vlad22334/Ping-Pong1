
from pygame import *
win_width = 700 win_height = 500 display.set_caption("Shooter") 
window = display.set_mode((win_width, win_height)) 
background = transform.scale(image.load(img_back), (win_width, win_height))
'''
class Player(sprite.Sprite):
    def __init__(self,x,y,size_x,size_y,speed):
        super().__init__()
        self.im = transform.scale(image.load('rocket.jpg'), (size_x,size_y))
        self.speed = speed

        self.rect = self.im.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

'''