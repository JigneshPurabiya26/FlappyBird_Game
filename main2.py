import pygame
import sys  # sys module will help us to exit the game
import random  # random module used to generate random numbers , will be used for generating random pipe

pygame.init()# this particular function initializes all the modules of the pygame module


# Now giving the height and width to the screen
width = 1300
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
        self.birdX = 100
        self.birdY = 100
        self.pipesX = [width,width+250,width+450,width+650,width+850,width+1050,width+1250]
        self.lowerPipeY = [self.randomPipe(),self.randomPipe(),self.randomPipe(),self.randomPipe(),self.randomPipe(),self.randomPipe(),self.randomPipe(),]
        self.upperPipeY = [self.randomRotatedPipe(),self.randomRotatedPipe(),self.randomRotatedPipe(),self.randomRotatedPipe(),self.randomRotatedPipe(),self.randomRotatedPipe(),self.randomRotatedPipe(),]
        self.gravity=0
        self.pipevel=0
        self.score=0


    def movingpipe(self):
        for i in range(0,7):
            self.pipesX [i] += -self.pipevel

        for i in range(0,7):
            if(self.pipesX[i] < -50):
                self.pipesX[i] = width + 100
                self.lowerPipeY[i] = self.randomPipe()
                self.upperPipeY[i] = self.randomRotatedPipe()

    def randomPipe(self):
        return random.randrange(int(height/2)+70, height-220) 
        #random.randrange function will give us random x,y coordinates 
        #here we have given the coordinates for the pipes
        #i.e for eg: if h=10 then h/2+2 is x i.e x=7 and h-2 will be y=8 so between these two numbers we can get the pipes

    def randomRotatedPipe(self):
        return random.randrange(-int(height/2)+70,-100)

    def mainGame(self):
        while self.gameOn:
            #event handling is done in the below code
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()    

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pipevel = 0.7

            #blitting images
            screen.blit(background,(0,0))

            for i in range(0,7):
                #lowerpipe
                screen.blit(pipe,(self.pipesX[i],self.lowerPipeY[i]))

                #upperpipe
                screen.blit(rotatedpipe,(self.pipesX[i],self.upperPipeY[i]))


            screen.blit(Bird, (self.birdX,self.birdY))

            #moving pipe
            self.movingpipe()

            pygame.display.update()


flappyBird = Game()
flappyBird.mainGame()