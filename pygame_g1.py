import pygame
from random import randint
import math
# initialize the screen
pygame.init()
# start the screen
layar = pygame.display.set_mode((800, 600))
score = 0
# judul game nya dan icon nya
pygame.display.set_caption("fox game made by itfoxguy ")
icon = pygame.image.load("fox.png")
pygame.display.set_icon(icon)

# player
playerimg = pygame.image.load('fox (1).png')
playerX = 370
playerY = 480
playerX_change = 0

# blueberry for foxy player uwu
blueberryimg = pygame.image.load('blueberry.png')
berryX = 370
berryY = 50


def player(x, y):
    layar.blit(playerimg, (x, y))


def blueberry(x, y):
    layar.blit(blueberryimg, (x, y))


def iscollision(berryx, berryy, playerx, playery):
    distance = math.sqrt(math.pow(berryx-playerx, 2) + math.pow(berryy-playery, 2))
    if distance < 27:
        return True
    else:
        return False


# def character(char, x, y):
#     layar.blit(char, (x, y))

# put backgound image to the code
background_img = pygame.image.load("the_first_background_for_game.png").convert()

running = True
# game loop
while running:
    # rgb for screen
    layar.fill((0, 0, 0))
    # detect the events in te screen
    for event in pygame.event.get():
        # to stop the game
        if event.type == pygame.QUIT:
            running = False
        # detect if a key is down
        if event.type == pygame.KEYDOWN:
            # if the key that is down is the left key, it makes it go left
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            # if the key that is down is the right key, it makes it go right
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        # detect if the key is up
        if event.type == pygame.KEYUP:
            # if the left and right key is not pushed, it stops
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # load in the background image to screen
    layar.blit(background_img, [0, 0])
    # the code below in order to change its x location
    playerX += playerX_change
    # code below so that the player does not come out of the screen
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # if it reach the bottom, it will come back up
    if berryY >= 600:
        berryY = 0
        berryX = randint(5, 731)
    else:
        berryY += 0.1
    # the bottom of this comment is for the feature for the score
    score_det_change = score
    # collision for fox and berry
    if iscollision(berryX, berryY, playerX, playerY):
        score += 1
        berryY = 0
        berryX = randint(5, 731)
    # print the score if the score is updated
    if score_det_change < score:
        score_det_change += 1
        print(int(score_det_change))
    blueberry(berryX, berryY)
    player(playerX, playerY)
    # character(blueberryimg, berryX, berryY)
    # character(playerimg, playerX, playerY)
    pygame.display.update()
print("let's code it up!!! ")
print('your total score was:', score)
