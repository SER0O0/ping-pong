import pygame
import sprite
from random import randint
from time import time as time
pygame.init()
from random import choice
from time import*

win_width = 700
win_height = 500

class GameSprite(sprite.Sprite):
#конструктор класса
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #вызываем конструктор класса (Sprite):
      sprite.Sprite.__init__(self)
      #каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect_x = player_x
      self.rect_y = player_y
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
      
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_W] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_S] and self.rect.y < win_height - 80:
           self.rect.y += self.speed

           



window = pygame.display.set_mode((500, 500))
window.fill((156, 47, 235))

game_over = False
move_left = False
move_right = False

speed_x = 3
speed_y = 3

class Area:
    def __init__(self, x, y, w, h, fill_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.fill_color = fill_color
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
class Sprite(Area):
    def __init__(self , x, y, w, h,  img_name):
        super().__init__(x, y, w, h,None)
        self.image = pygame.image.load(img_name)

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

ball = GameSprite('ball.png', 250, 250, 50, 50,3 )
platform1 = Player('platform.png', 400, 250, 25, 99,3)
platform2 = Player('platform.png', 100, 250, 25, 99,3)

while game:
    window.blit(window,(0,0))

    for b in event.get():
        if b.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(window,(0,0))
        ball.update()
        platform1.update()
        platform2.update()

        ball.reset()
        platform1.reset()
        platform2.reset()
        final.reset()

    

    if ball.collide_rect(platform1,platform2):
        player_x * -1
    if player_y < 0 or player_y > 500:
        player_y * -1
        
    if sprite.collide_rect(final):
        finish = True

if player_x < 0 :
    text = '2 игрок выйграл'
if player_x > 500:
    text = '1 игрок выйграл'

f = pygame.font.SysFont('Arial', 80)
text = f.render(text, True, (255, 0, 0))
window.blit(text, (160, 200))
pygame.display.update()















