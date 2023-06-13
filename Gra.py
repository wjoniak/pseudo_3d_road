import sys
import pygame
import random
# Otwarcie gry
pygame.init()
res = (720, 720)
#
c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)
display = pygame.display.set_mode(res)
clock = pygame.time.Clock()
colox_c1 = 0
colox_c2 = 0
colox_c3 = 254
colox_c4 = 254
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color_list = [red, green, blue]
# Przypisanie koloru
player_c = random.choice(color_list)
# Kolory przycisków w Menu
startl = (169, 169, 169)
startd = (100, 100, 100)
white = (255, 255, 255)
start = (255, 255, 255)
width = display.get_width()
height = display.get_height()
# Pozycja startowa gracza
lead_x = 40
lead_y = height / 2
x = 300
y = 290
width1 = 100
height1 = 40
enemy_size = 50
# Czcionka
smallfont = pygame.font.SysFont('Corbel', 35)
# UI
text = smallfont.render('Start', True, white)
text1 = smallfont.render('Options', True, white)
exit1 = smallfont.render('Exit', True, white)
colox = smallfont.render('Colox', True, (c3, c2, c1))
x1 = random.randint(width / 2, width)
y1 = random.randint(100, height / 2)
x2 = 40
y2 = 40
speed = 15
# Punkty gracza
count = 0
rgb = random.choice(color_list)
e_p = [width, random.randint(50, height - 50)]
e1_p = [random.randint(width, width + 100), random.randint(50, height
- 100)]
# GEJM OVA
def game_over():
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:

                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
            if height - 100 < mouse1[1] < height - 80 and 100 < mouse1[0] < 140:
    # Koniec
    pygame.quit()
    if ev.type == pygame.MOUSEBUTTONDOWN:
    if height - 100 < mouse1[1] < height - 80 and width - 180 < mouse1[0] < width - 100:
    game(lead_x, lead_y, speed, count)

    display.fill((65, 25, 64))
    smallfont = pygame.font.SysFont('Corbel', 60)
    smallfont1 = pygame.font.SysFont('Corbel', 25)
    game_over = smallfont.render('GAME OVER', True, white)
    game_exit = smallfont1.render('exit', True, white)
    restart = smallfont1.render('restart', True, white)
    mouse1 = pygame.mouse.get_pos()
    #Przycisk końca gry
    if height - 100 < mouse1[1] < height - 80 and 100 < mouse1[0] < 140:
    pygame.draw.rect(display, startl, [100, height - 100, 40,20])
    else:
    pygame.draw.rect(display, startd, [100, height - 100, 40,20])
    # Zacznij jeszcze raz
    if height - 100 < mouse1[1] < height - 80 and width - 180 < mouse1[0] < width - 100:
    pygame.draw.rect(display, startl, [width - 180, height- 100, 80, 20])
    else:
    pygame.draw.rect(display, startd, [width - 180, height- 100, 80, 20])
    display.blit(game_exit, (100, height - 100))
    display.blit(restart, (width - 180, height - 100))
    display.blit(game_over, (width / 2 - 150, 295))
    pygame.display.update()
    pygame.draw.rect(display, startd, [100, height - 100, 40, 20])
    pygame.draw.rect(display, startd, [width - 180, height - 100, 40, 50])

def game(lead_y,lead_X,speed,count,):
while True:
for ev in pygame.event.get():
if ev.type == pygame.QUIT:
pygame.quit()
keys = pygame.key.get_pressed()
if keys[pygame.K_UP]:
# Przycisk, wraz z wcisnięciem, zmiana pozycji  gracza o 10 pikseli
lead_y -= 10
if keys[pygame.K_DOWN]:
# ----||------ wzrasta kf
lead_y += 10
display.fill((65, 25, 64))
clock.tick(speed)
rect = pygame.draw.rect(display, player_c, [lead_x, lead_y, 40,40])
pygame.draw.rect(display, (c1, c2, c3), [0, 0, width, 40])
pygame.draw.rect(display, (c3, c2, c1), [0, 680, width, 40])
pygame.draw.rect(display, startd, [width - 100, 0, 100, 40])
smallfont = pygame.font.SysFont('Corbel', 35)
exit2 = smallfont.render('Exit', True, white)
mouse = pygame.mouse.get_pos()
if 0 < mouse[1] < 40 and width - 100 < mouse[0] < width:
pygame.draw.rect(display, startl, [width - 100, 0, 100, 40])
else:
pygame.draw.rect(display, startd, [width - 100, 0, 100, 40])
if 0 < mouse[1] < 40 and width - 100 < mouse[0] < width:
if ev.type == pygame.MOUSEBUTTONDOWN:
pygame.quit()
# Pozycja negatywnych puntków
if e_p[0] <= width and e_p[0] > 0:
e_p[0] -= 10
else:
if e_p[1] >= height - 40 or e_p[1] <= 40:
e_p[1] = height / 2
if e1_p[1] >= height - 40 or e1_p[1] <= 40:
e1_p[1] = random.randint(40, height - 40)
e_p[1] = random.randint(enemy_size, height - enemy_size)
e_p[0] = width
# KONIEC GRY w tyn przypadu
if lead_y >= e_p[1] >= lead_y - 40 and lead_x <= e_p[0] <= lead_x + 40:
game_over()
# Zderzenie z graczem
if lead_x <= e_p[0] <= lead_x + 40 and lead_y <= e_p[1] + enemy_size <= lead_y + 40:
game_over()
pygame.draw.rect(display, red, [e_p[0], e_p[1], enemy_size,enemy_size])
if e1_p[0] <= width + 100 and e1_p[0] > 0:
e1_p[0] -= 10
else:
if e1_p[1] >= height - 40 or e1_p[1] <= 40:
e1_p[1] = height / 2
e1_p[1] = random.randint(enemy_size, height - 40)
e1_p[0] = width + 100
if lead_y >= e1_p[1] >= lead_y - 40 and lead_x <= e1_p[0] <= lead_x + 40:
e1_p[0] = width + 100
e1_p[1] = random.randint(40, height - 40)
count += 1
speed += 1
if lead_x <= e1_p[0] <= lead_x + 40 and lead_y <= e1_p[1] + enemy_size <= lead_y + 40:
e1_p[0] = width + 100
e1_p[1] = random.randint(40, height - 40)
# Wzrost punktów
count += 1
# Z wrsitem puntków wzrasta prędkosć
speed += 1
if count >= 45:
# Prędkość maksymalna
speed = 60
if lead_y >= height - 38 or lead_y <= 38:
game_over()
if e1_p[0] <= 0:
game_over()
pygame.draw.rect(display, blue, [e1_p[0], e1_p[1], enemy_size,
enemy_size])
score1 = smallfont.render('Score:', True, white)
display.blit(score1, (width - 120, height - 40))
display.blit(exit2, (width - 80, 0))
pygame.display.update()
# UI
def intro(colox_c1,colox_c2,colox,exit1,text1,text,):
intro = True
while intro:
for event in pygame.event.get():
if event.type == pygame.QUIT:
pygame.quit()
display.fill((65, 25, 64))
mouse = pygame.mouse.get_pos()
# Menu startowe
if y < mouse[1] < y + height1 and x < mouse[0] < x + width1:
# Estetyka (ocieniowanie najechanego przycisku)
pygame.draw.rect(display, startl, [x, y, width1, height1])
else:
if y + 70 < mouse[1] < y + 70 + height1 and x < mouse[0] < x + width1 + 40:
pygame.draw.rect(display, startl, [x, y + 70, width1+40,height1])
else:
if y + 140 < mouse[1] < y + 140 + height1 and x < mouse[0] < width1 + x:
pygame.draw.rect(display, startl, [x, y + 140,width1,height1])
else:
pygame.draw.rect(display, startd, [x, y, width1,height1])
pygame.draw.rect(display, startd, [x, y + 70, width1 + 40, height1])
pygame.draw.rect(display, startd, [x, y + 140,width1, height1])
# START gry
if event.type == pygame.MOUSEBUTTONDOWN:
if x < mouse[0] < x + width1 and y < mouse[1] < y + height1:
game(lead_y, lead_x, speed, count)
if event.type == pygame.MOUSEBUTTONDOWN:
if x < mouse[0] < width1 + x and y + 140 < mouse[1] < y + 140 + height1:
pygame.quit()
#Kolory
if 0 <= colox_c2 <= 254 or 0 <= colox_c1 <= 254:
colox_c1 += 1
colox_c2 += 1
if colox_c2 >= 254 or colox_c1 >= 254:
colox_c1 = c3
colox_c2 = c3
pygame.draw.rect(display, (c2, colox_c1, colox_c2), [0, 0, 40,
height])
pygame.draw.rect(display, (c2, colox_c1, colox_c2), [width - 40,
0, 40, height])
smallfont = pygame.font.SysFont('Corbel', 35)
sig = smallfont.render('Designed by :- Antriksh', True, white)
text = smallfont.render('Start', True, white)
text1 = smallfont.render('Options', True, white)
exit1 = smallfont.render('Exit', True, white)
colox = smallfont.render('Colox', True, (c1, colox_c1,
colox_c2))
display.blit(colox, (312, 50))
display.blit(text, (312, 295))
display.blit(text1, (312, 365))
display.blit(exit1, (312, 435))
display.blit(sig, (320, height - 50))
clock.tick(60)
pygame.display.update()
intro(colox_c1,colox_c2,colox,exit1,text1,text,)