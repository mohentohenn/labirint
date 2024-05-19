from pygame import *
from time import *

class GameSprite(sprite.Sprite):
    def __init__(self,picture,w,h,x,y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self,picture, w, h, x, y, x_speed, y_speed):
        super().__init__(picture, w, h, x, y)     
        self.x_speed = x_speed
        self.y_speed = y_speed   
    def update(self):
        self.rect.x+=self.x_speed
        self.rect.y+=self.y_speed

window = display.set_mode((900, 800))
display.set_caption('Вейдер в лабиринте')
picture = GameSprite('doni.png',900,800, 0, 0)
picture_2 = GameSprite('donidonidoni.png',900,800, 0, 0)

vader = Player('vader.png', 150,150,100,100,0,0)

run = True
while run:

 #   wall_1.reset()
  #  wall_2.reset()
    picture.reset()
    picture_2.reset()
    vader.reset()

  

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                vader.y_speed = -5
            elif e.key == K_DOWN:
                vader.y_speed = 5   
            elif e.key == K_LEFT:
                vader.x_speed = -5
            elif e.key == K_RIGHT:
                vader.x_speed = 5
        elif e.type == KEYUP:
            if e.key == K_UP or e.key == K_DOWN:
                vader.y_speed = 0
            elif e.key == K_LEFT or e.key == K_RIGHT:
                vader.x_speed = 0
    vader.update()
    vader.reset()
    display.update()        

                
                    




