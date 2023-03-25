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
    

speed_x = 3
speed_y = 2
font.init()
font = font.SysFont("Calibri", 30)
lose1 = font.render('PLAYER 1 LOST!',True, (0, 0, 0))
lose2 = font.render('PLAYER 2 LOST!', True, (0, 0, 0))
window = display.set_mode((800, 500))
display.set_caption("Ping Pong")
background = transform.scale(image.load("Ping-pong/pingpong.jpg"), (800, 500))
line1 = Player('Ping-pong/line1.jpg', 10, 200, 50, 150, 10)
line2 = Player('Ping-pong/line2.jpg', 740, 200, 50, 150, 10)
ball = GameSprite('Ping-pong/ball.png', 400, 250, 30, 30, 50)
#parameters of the image sprite

#game loop
run = True
finish = False
clock = time.Clock()
FPS = 80

while run:

    if finish != True:
        window.blit(background,(0, 0))
        line2.update()
        line1.update2()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(line1, ball) or sprite.collide_rect(line2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > 500-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (400, 250))
            game_over = True


        if ball.rect.x > 800:
            finish = True
            window.blit(lose2, (400, 250))
            game_over = True

    for e in event.get():
        if e.type == QUIT:
            run = False

    line1.reset()
    line2.reset()
    ball.reset()

    display.update ()
    clock.tick(FPS)
