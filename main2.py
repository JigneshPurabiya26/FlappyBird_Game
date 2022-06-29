import pygame
import sys  # sys module will help us to exit the game
import random  # random module used to generate random numbers , will be used for generating random pipe

pygame.init()# this particular function initializes all the modules of the pygame module


# Now giving the height and width to the screen
width = 1100
height = 620

# now creating the display using the function pygame.display.set_mode
screen = pygame.display.set_mode((width, height))

# Now loading the images; we have declared them as global variables
background = pygame.image.load("Sprites/Background Image.png").convert_alpha()
Bird = pygame.image.load("Sprites/Bird.png").convert_alpha()
pipe = pygame.image.load("Sprites/Pipe.png").convert_alpha()
rotatedpipe = pygame.image.load("Sprites/rotated_pipe.png").convert_alpha()

# loading the sounds
hit = pygame.mixer.Sound('Audio/sounds_sfx_hit.wav')
point = pygame.mixer.Sound('Audio/sounds_sfx_point.wav')
flap = pygame.mixer.Sound('Audio/wingflap_fast-7139.wav')

#game caption                
pygame.display.set_caption('Flappy Bird by Jignesh')

class Game:
    def __init__(self):
        self.gameOn = True
        self.BirdX = 100
        self.BirdY = 100

    def mainGame(self):
        while self.gameOn:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    


            #blitting images
            screen.blit(background,(0,0))
            screen.blit(Bird, (self.BirdX,self.BirdY))

            pygame.display.update()


flappyBird = Game()
flappyBird.mainGame()