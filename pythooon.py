from pygame import*
from random import randint

font.init()
font1 = font.Font(None, 80)
win = font1.render('You WIN!', True, (235, 235, 235))
lose = font1.render('YOU NOOB!', True, (170, 0, 0))
font2 = font.Font(None, 36)

img_ball = "ball.png"
img_bg = "bg.jpg"

win_width = 700
win_height = 500
display.set_caption("Pin-Pong")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_bg), (win_width, win_height))

game = True
while game:
    window.blit(background,(0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
      
    display.update()

sprite1 = transform.csale(image.load("ball.png")), (100, 100)

window.blit(sprite1), (x100, y100)