from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressd = key.get_pressed()
        if keys_pressd[K_UP] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys_pressd[K_DOWN] and self.rect.y:
            self.rect.y += self.speed

    def update2(self):
        keys_pressd = key.get_pressed()
        if keys_pressd[K_w] and self.rect.y > self.speed:
            self.rect.y -= self.speed
        if keys_pressd[K_s] and self.rect.y:
            self.rect.y += self.speed


font.init()
font2 = font.SysFont("Calibri", 30)
window = display.set_mode((700, 500))
display.set_caption("Ping Pong")
background = transform.scale(image.load("Ping-pong/pingpong.jpg"), (700, 500))
line1 = Player('Ping-pong/line1.jpg', 30, 200, 50, 150, 4)
line2 = Player('Ping-pong/line2.jpg', 630, 200, 50, 150, 4)
#parameters of the image sprite

#game loop
run = True
finish = False
clock = time.Clock()
FPS = 80

while run:

    if finish != True:
        window.blit(background,(0, 0))
        line1.update2()

    line1.reset()
    line2.reset()

    display.update ()
    clock.tick(FPS)
