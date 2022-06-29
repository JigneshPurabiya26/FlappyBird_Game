import pygame
import sys  # sys module will help us to exit the game
import random  # random module used to generate random numbers , will be used for generating random pipe
from pygame.locals import *

pygame.init()# this particular function initializes all the modules of the pygame module


# we have given the screen refresh rate here
FPS = 32

# Now giving the height and width to the screen
width = 1270
height = 720

# now creating the display using the function pygame.display.set_mode
screen = pygame.display.set_mode((width, height))

# Now loading the images; we have declared them as global variables
background = pygame.image.load("Sprites/Background Image.png").convert_alpha()
Bird = pygame.image.load("Sprites/Bird.png").convert_alpha()
pipe = pygame.image.load("Sprites/Pipe.png").convert_alpha()
GroundY = height*0.8
Game_Sprites = {}
Game_Sounds = {}

# loading the sounds
hit = pygame.mixer.Sound('Audio/sounds_sfx_hit.wav')
point = pygame.mixer.Sound('Audio/sounds_sfx_point.wav')
flap = pygame.mixer.Sound('Audio/wingflap_fast-7139.wav')

if __name__ == "__main__":
    # this will be the main point from where our game will start
    FPSCLOCK = pygame.time.Clock()  # the clock is used to control the fps of the game
    pygame.display.set_caption('Flappy Bird by Jignesh')

    # Now here we have created a dictionary which has key named as numbers
    # convert_alpha is used to optimize our images for gaming i.e. works with the pixels of the image for faster blitting
    Game_Sprites['numbers'] = (
        pygame.image.load('Sprites/0-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/1-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/2-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/3-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/4-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/5-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/6-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/7-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/8-Number-PNG.png').convert_alpha(),
        pygame.image.load('Sprites/9-Number-PNG.png').convert_alpha(),
    )

    Game_Sprites['pipe'] = (
        pygame.transform.rotate(pygame.image.load(pipe).convert_alpha(), 180),  # reverse pipe
        pygame.image.load(pipe).convert_alpha()
    )
    Game_Sprites['background'] = pygame.image.load(background).convert()
    Game_Sprites['bird'] = pygame.image.load(Bird).convert_alpha()
    Game_Sprites['base'] = pygame.image.load("Sprites/base.png").convert_alpha()


# Game Sounds
Game_Sounds['hit'] = pygame.mixer.Sound(hit)
Game_Sounds['point'] = pygame.mixer.Sound(point)
Game_Sounds['flap'] = pygame.mixer.Sound(flap)

while True:
    mainGame() #this is the main game function