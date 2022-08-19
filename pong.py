import pygame
from pygame import*
import sys
from paddle import Paddle
from ball import Ball

pygame.init()
black = (0 , 0 , 0)
white = (255 , 255 , 255)
BLUE =  (  0,   40, 255)
GREEN =   (0,  255,0)

size = (800 , 600)
game_display = pygame.display.set_mode(size)
pygame.display.set_caption('pong')

paddel1 = Paddle(BLUE , 10 , 100)
paddel1.rect.x = 25
paddel1.rect.y = 250

paddel2 = Paddle(GREEN , 10 , 100)
paddel2.rect.x = 765
paddel2.rect.y = 250

ball = Ball(white , 15 , 15)
ball.rect.x = 300
ball.rect.y = 150

clock = pygame.time.Clock()

score1 = 0
score2 = 0

poping_sound = pygame.mixer.Sound('poping.wav')
scoring_sound = pygame.mixer.Sound('scoring.wav')


game_on = True
sprites_list = pygame.sprite.Group()
sprites_list.add(paddel1)
sprites_list.add(paddel2)
sprites_list.add(ball)

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                game_on = False
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddel1.paddles_moving_up(7)
    if keys[pygame.K_s]:
        paddel1.paddles_moving_down(7)
    if keys[pygame.K_UP]:
        paddel2.paddles_moving_up(7)
    if keys[pygame.K_DOWN]:
        paddel2.paddles_moving_down(7)

    sprites_list.update()

    if ball.rect.x >= 780:
        score1 += 1
        scoring_sound.play()
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 400
        ball.rect.y = 200

    if ball.rect.x <= 2:
        score2 += 1
        scoring_sound.play()
        ball.velocity[0] = -ball.velocity[0]
        ball.rect.x = 400
        ball.rect.y = 200

    if ball.rect.y > 580:
        ball.velocity[1] = -ball.velocity[1]

    if ball.rect.y < 2:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball , paddel1) or pygame.sprite.collide_mask(ball , paddel2):
        ball.bouncing()
        poping_sound.play()

    game_display.fill(black)
    pygame.draw.line(game_display , white , [400 , 0] , [400 , 600] , 5)
    sprites_list.draw(game_display)

    font = pygame.font.Font(None , 100)
    text = font.render(str(score1) , 1 , white)
    game_display.blit(text , (305 , 10))

    text = font.render(str(score2) , 1 , white)
    game_display.blit(text , (420 , 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
