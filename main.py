import math
import random
import pygame
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((1200,800))

background = pygame.image.load('F:\PythonElements/background.png')


pygame.display.set_caption("Space Invaders")
icon  = pygame.image.load('F:\PythonElements/ufo.png')
pygame.display.set_icon(icon)

mixer.music.load('F:\PythonElements/background.wav')
mixer.music.play(-1)

score_value = 0
font = pygame.font.Font('freesansbold.ttf',64)
over_font = pygame.font.Font('freesansbold.ttf',128)
winning_font = pygame.font.Font('freesansbold.ttf',128)
textX = 10
textY = 10

playerImg = pygame.image.load('F:\PythonElements/battleship.png')
class player():
    def __init__(self,Img,x,y,X_change,Y_change):
        self.Img = Img
        self.x = x
        self.y = y
        self.X_change = X_change
        self.Y_change = Y_change

    def show_player(self):
        screen.blit(self.Img, (self.x,self.y))

playerX = 600
playerY = 650
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('F:\PythonElements/monster.png')
enemy2Img = pygame.image.load('F:\PythonElements/monster_lv2.png')
enemy3Img = pygame.image.load('F:\PythonElements/monster_bosslv.png')
enemy4Img = pygame.image.load('F:\PythonElements/monster_boss2.png')

class enemy():
    def __init__(self,Img,x,y,X_change,Y_change):
        self.Img = Img
        self.x = x
        self.y = y
        self.X_change = X_change
        self.Y_change = Y_change

    def show_enemy(self):
        screen.blit(self.Img,(self.x,self.y))

    def off_screen(self):

        self.x = random.randint(1350,1400)
        self.y = random.randint(1050,1100)
        self.X_change = 0
        self.Y_change = 0
    def move(self):
        self.x += self.X_change
        if self.x <= 0:
            self.X_change = 3
            self.y += self.Y_change
        elif self.x >= 1134:
            self.X_change = -3
            self.y += self.Y_change
    def show_lv(self):
        print("monster_lv1 is dead!")
    def show_xy(self):
        print("x = :",self.x,"y = : ",self.y)
class enemy2(enemy):
    def __init__(self,Img,x,y,X_change,Y_change):
        self.Img = Img
        self.x = x
        self.y = y
        self.X_change = X_change
        self.Y_change = Y_change
    def show_lv2(self):
        print("monster_lv2 is dead!")
class enemy3(enemy):
    def __init__(self, Img, x, y, X_change, Y_change):
        self.Img = Img
        self.x = x
        self.y = y
        self.X_change = X_change
        self.Y_change = Y_change
    def show_lv3(self):
        print("monster_lv3 is dead!")
class boss(enemy):
    def __init__(self, Img, x, y, X_change, Y_change):
        self.Img = Img
        self.x = x
        self.y = y
        self.X_change = X_change
        self.Y_change = Y_change
    def show_boss(self):
        screen.blit(self.Img, (self.x, self.y))
    def show_xychange(self):
        print("x_change = :",self.X_change,"y_change = : " ,self.Y_change)

bulletImg = pygame.image.load('F:\PythonElements/bullet.png')
class bullet():
    def __init__(self,Img,x,y,X_change,Y_change,state):
        self.Img = Img
        self.x = x
        self.y  = y
        self.X_chanage = X_change
        self.Y_change = Y_change
        self.state = state

    def fire_bullet(self):
        self.state = "fire"
        screen.blit(self.Img, (self.x + 5, self.y + 10))

num_of_enemies = random.randint(5,9)


def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(0,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    game_over = over_font.render("Game Over!" ,True,(255,0,0))
    screen.blit(game_over, (300,300))
def winning_text():
    winning = winning_font.render("You win!",True,(255,0,0))
    screen.blit(winning,(350,300))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance <47:
        return True
    else:
        return False

def isCollision2(playerX,playerY,enemyX,enemyY):
    distance = math.sqrt((math.pow(playerX-enemyX,2)) + (math.pow(playerY-enemyY,2)))
    if distance <47:
        return True
    else:
        return False
num_losinglife = True
movement = True
running = True
level = 0
player = player(playerImg,600,650,0,0)
bullet = bullet(bulletImg,0,650,0,10,"ready")
enemy_boss = boss(enemy4Img,600,0,3,40)
eliminate_num = 0
enemylv1 = []
enemylv2 = []
enemylv3 = []
boss_health = 3


for i in range(num_of_enemies):
    enemylv1.append(enemy(enemyImg,random.randint(0,1050),random.randint(20,120),5,40))
    enemylv2.append(enemy2(enemy2Img, random.randint(0, 1050), random.randint(20,120), 5, 40))
    enemylv3.append(enemy3(enemy3Img, random.randint(0, 1050), random.randint(20,120), 5, 40))

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if movement == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.Y_change = -5
                if event.key == pygame.K_DOWN:
                    player.Y_change = 5
                if event.key == pygame.K_LEFT:
                    player.X_change = -5
                if event.key == pygame.K_RIGHT:
                    player.X_change = 5
                if event.key == pygame.K_SPACE:
                    if bullet.state == "ready":
                        bullet_Sound = mixer.Sound('F:\PythonElements/laser.wav')
                        bullet_Sound.play()
                        bullet.x = player.x
                        bullet.fire_bullet()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.X_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player.Y_change = 0

    player.x += player.X_change
    player.y += player.Y_change
    if player.x <= 0:
        player.x = 0
    elif player.x >= 1134:
        player.x = 1134
    if player.y <= 0:
        player.y = 0
    elif player.y >=734:
        player.y = 734
    # collision between bullet and enemy
    if level == 0:
        for i in range(num_of_enemies):
            enemylv1[i].show_enemy()
            enemylv1[i].move()
            collision_lv1 = isCollision(enemylv1[i].x, enemylv1[i].y, bullet.x, bullet.y)
            collision_player = isCollision2(player.x, player.y, enemylv1[i].x, enemylv1[i].y)
            if collision_lv1:
                elimination_Sound = mixer.Sound('F:\PythonElements/elimination.wav')
                elimination_Sound.play()
                bullet.y = player.y
                bullet.state = "ready"
                score_value += 1
                eliminate_num += 1
                enemylv1[i].off_screen()
                if eliminate_num == num_of_enemies:
                    level += 1
                    eliminate_num = 0
            if collision_player:
                if num_losinglife == True:
                    losinglife_Sound = mixer.Sound('F:\PythonElements/losinglife.wav')
                    losinglife_Sound.play()
                num_losinglife = False
                movement = False
                mixer.music.stop()
                game_over_text()
            if movement == False:
                enemylv1[i].X_change = 0
                enemylv1[i].Y_change = 0
    elif level == 1:
        for i in range(num_of_enemies):
            enemylv2[i].show_enemy()
            enemylv2[i].move()
            collision_lv2 = isCollision(enemylv2[i].x, enemylv2[i].y, bullet.x, bullet.y)
            collision_player = isCollision2(player.x, player.y, enemylv2[i].x, enemylv2[i].y)
            if collision_lv2:
                elimination_Sound = mixer.Sound('F:\PythonElements/elimination.wav')
                elimination_Sound.play()
                bullet.y = player.y
                bullet.state = "ready"
                score_value += 1
                eliminate_num += 1
                enemylv2[i].off_screen()
                if eliminate_num == num_of_enemies:
                    level += 1
                    eliminate_num = 0
            if collision_player:
                if num_losinglife == True:
                    losinglife_Sound = mixer.Sound('F:\PythonElements/losinglife.wav')
                    losinglife_Sound.play()
                num_losinglife = False
                movement = False
                mixer.music.stop()
                game_over_text()
            if movement == False:
                enemylv2[i].X_change = 0
                enemylv2[i].Y_change = 0
    if level == 2:
        for i in range(num_of_enemies):
            enemylv3[i].show_enemy()
            enemy_boss.show_boss()
            enemylv3[i].move()
            collision_lv3 = isCollision(enemylv3[i].x, enemylv3[i].y, bullet.x, bullet.y)
            collision_boss = isCollision(enemy_boss.x, enemy_boss.y, bullet.x, bullet.y)
            collision_player = isCollision2(player.x, player.y, enemylv3[i].x, enemylv3[i].y)
            collision_playerboss = isCollision2(player.x, player.y, enemy_boss.x, enemy_boss.y)
            if collision_lv3:
                elimination_Sound = mixer.Sound('F:\PythonElements/elimination.wav')
                elimination_Sound.play()
                bullet.y = player.y
                bullet.state = "ready"
                score_value += 1
                eliminate_num += 1
                enemylv3[i].off_screen()
            if collision_boss:
                elimination_Sound = mixer.Sound('F:\PythonElements/elimination.wav')
                elimination_Sound.play()
                bullet.y = player.y
                bullet.state = "ready"
                boss_health -= 1
                if boss_health == 0:
                    score_value += 1
                    eliminate_num += 1
                    enemy_boss.off_screen()
            if score_value == (num_of_enemies * 3) + 1:
                winning_Sound = mixer.Sound('F:\PythonElements/winning.wav')
                movement = False
                winning_text()
            if collision_player or collision_playerboss:
                if num_losinglife == True:
                    losinglife_Sound = mixer.Sound('F:\PythonElements/losinglife.wav')
                    losinglife_Sound.play()
                num_losinglife = False
                movement = False
                mixer.music.stop()
                game_over_text()
            if movement == False:
                enemylv3[i].X_change = 0
                enemylv3[i].Y_change = 0
                enemy_boss.X_change = 0
                enemy_boss.Y_change = 0
    enemy_boss.move()

    if bullet.y <=0:
        bullet.y = player.y
        bullet.state = "ready"

    if bullet.state == "fire":
        bullet.fire_bullet()
        bullet.y -= bullet.Y_change

    player.show_player()
    show_score(textX,textY)
    pygame.display.update()