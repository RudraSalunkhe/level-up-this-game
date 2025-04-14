import math
import random
import pygame

width1=500
height1=500
player_x_coordinate=370
player_y_coordinate=380
enemy_y_coordinate_min=50
enemy_y_coordinate_max=150
enemy_speed_x=4
enemy_speed_y=40
laser_speed_y=10
collision_distance=27

pygame.init()
screen=pygame.display.set_mode((width1,height1))

background=pygame.image.load("bg.png")

pygame.display.set_caption("my first game")
icon=pygame.image.load("icon.png")
pygame.display.set_icon(icon)

playerimg=pygame.image.load("ufo.png")
playerx=player_x_coordinate
playery=player_y_coordinate
playerx_change=0

enemyImg=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
num_of_enemy=7

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemy_x.append(random.randint(0,width1-64))

    enemy_y.append(random.randint(enemy_y_coordinate_min,enemy_y_coordinate_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

laserImg=pygame.image.load("laser.png")
laser_x=0
laser_y=player_y_coordinate
laser_x_change=0
laser_y_change=laser_speed_y
laser_state="ready"

score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textx=0
texty=0

over_font=pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score=font.render('score :'+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text=over_font.render('GAME OVER',True,(255,255,255))
    screen.blit(over_text,(200,250))

def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="free"
    screen.blit(laserImg,(x+16,y+10))

def iscollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt((enemyx-bulletx)**2+(enemyy-bullety)**2)
    return distance<collision_distance

running=True
while  running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playery_change=-5
            if event.key==pygame.K_RIGHT:
                playerx_change=5
            if event.key==pygame.K_SPACE and bullet_state=="ready":
                bulletx=playerx
            fire_bullet(bulletx,bullety)
        if event.type==pygame.KEYUP and event.key in (pygame.K_LEFT,pygame.K_RIGHT):
            playerx_change=0

    playerx=playerx_change
    playerx=max(0,min(playerx,screen_width-64))

    for i in range (num_of_enemy):
        if enemyy[i]>340:
            for j in range(num_of_enemy):
                enemyy[j]=2000
            game_over_text()
            break
        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0 or enemyx[i]>=screen_width-64:
            enemyx_change[i]*=-1
            enemyy[i]+=enemyy_change[i]
        if iscollision(enemyx[i],enemyy[i],bulletx,bullety):
            bullety=player_start_y
            bullet_state="ready"
            score_value+=1
            enemyx[i]=random.randint(0,screen_width-64)
            enemyy[i]=random.randint(enemy_start_y_min,enemy_start_y_max)
        enemy(enemyx[i],enemyy[i],i)

    if bullety<=0:
        bullety=player_start_y
        bullet_state="ready"
    elif bullet_state=="fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
    player(playerx,playery)
    show_score(textx,texty)
    pygame.display.update()








