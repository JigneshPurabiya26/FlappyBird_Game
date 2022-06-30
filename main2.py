import pygame
import sys  # sys module will help us to exit the game
import random  # random module used to generate random numbers , will be used for generating random pipe

pygame.init()  # this particular function initializes all the modules of the pygame module


# Now giving the height and width to the screen
width = 1300
height = 630
clock = pygame.time.Clock()
fps = 60

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

# game caption
pygame.display.set_caption('Flappy Bird by Jignesh')


class Game:
    def __init__(self):
        self.gameOn = True
        self.birdX = 100
        self.birdY = 100
        self.pipesX = [width, width+250, width+450,
                       width+650, width+850, width+1050, width+1250]
        self.lowerPipeY = [self.randomPipe(), self.randomPipe(), self.randomPipe(
        ), self.randomPipe(), self.randomPipe(), self.randomPipe(), self.randomPipe(), ]
        self.upperPipeY = [self.randomRotatedPipe(), self.randomRotatedPipe(), self.randomRotatedPipe(
        ), self.randomRotatedPipe(), self.randomRotatedPipe(), self.randomRotatedPipe(), self.randomRotatedPipe(), ]
        self.gravity = 0
        self.pipevel = 0
        self.score = 0
        self.flap = 0
        self.rotateangle = 0
        self.isgameover = False
        self.playSound = True

    def movingpipe(self):
        for i in range(0, 7):
            self.pipesX[i] += -self.pipevel

        for i in range(0, 7):
            if(self.pipesX[i] < -50):
                self.pipesX[i] = width + 100
                self.lowerPipeY[i] = self.randomPipe()
                self.upperPipeY[i] = self.randomRotatedPipe()

    def randomPipe(self):
        return random.randrange(int(height/2)+80, height-220)
        # random.randrange function will give us random x,y coordinates
        # here we have given the coordinates for the pipes
        # i.e for eg: if h=10 then h/2+2 is x i.e x=7 and h-2 will be y=8 so between these two numbers we can get the pipes

    def randomRotatedPipe(self):
        return random.randrange(-int(height/2)+70, -170)

    def flapping(self):
        self.birdY += self.gravity
        if(self.isgameover == False):
            self.flap -= 1  # - because we need to go upwards
            self.birdY -= self.flap

    def iscollide(self):
        for i in range(0, 7):
            if(self.birdX >= self.pipesX[i] and self.birdX <= (self.pipesX[i]+pipe.get_width())
                and ((self.birdY+Bird.get_height()-15) >= self.lowerPipeY[i] or
                     (self.birdY) <= self.upperPipeY[i] + rotatedpipe.get_height()-15)):
                return True

            elif(self.birdX == self.pipesX[i] and (self.birdY <= self.lowerPipeY[i] and self.birdY >= self.upperPipeY[i])):
                if(self.isgameover == False):
                    self.score += 1
                    pygame.mixer.Sound.play(point)

        if(self.birdY <= 0):
            return True

        elif(self.birdY + Bird.get_height() >= height):
            self.gravity = 0
            return True

    def gameOver(self):
        if(self.iscollide()):
            self.isgameover = True
            self.screenText("Game Over !",(255,255,255),450,200,50,"Century Gothic",bold=True)
            self.screenText("Press Enter to play again",(255,255,255),450,400,48,"Century Gothic",bold=True)
            self.pipevel = 0
            self.flap = 0
            self.rotateangle = -90
            if(self.playSound):
                pygame.mixer.Sound.play(hit)
                self.playSound=False

    def screenText(self,text,color,x,y,size,style,bold=False):
        font = pygame.font.SysFont(style,size,bold=bold)
        screen_text = font.render(text,True,color)
        screen.blit(screen_text,(x,y))

    def mainGame(self):
        while self.gameOn:
            # event handling is done in the below code
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # when x is clicked by mouse
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # keydown means the key is pressed
                    if event.key == pygame.K_SPACE:  # when space is clicked
                        if(self.isgameover==False):
                            self.pipevel = 3.5
                            self.gravity = 3
                            self.flap = 15
                            self.rotateangle = 15  

                    if event.key == pygame.K_RETURN:
                        newGame = Game()
                        newGame.mainGame()

                if event.type == pygame.KEYUP:  # keyup means the key is realsed
                    if event.key == pygame.K_SPACE:
                        self.rotateangle = 0
     

            # blitting images
            screen.blit(background, (0, 0))

            for i in range(0, 7):
                # lowerpipe
                screen.blit(pipe, (self.pipesX[i], self.lowerPipeY[i]))

                # upperpipe
                screen.blit(rotatedpipe, (self.pipesX[i], self.upperPipeY[i]))

            screen.blit(pygame.transform.rotozoom(
                Bird, self.rotateangle, 1), (self.birdX, self.birdY))

            # moving pipe
            self.movingpipe()

            # Flapping
            self.flapping()

            # gameover
            self.gameOver()

            #Score
            # self.screenText(str(self.score),(255,255,255),450,100,50,"Century Gothic",bold=True)


            pygame.display.update()
            clock.tick(fps)


flappyBird = Game()
flappyBird.mainGame()
