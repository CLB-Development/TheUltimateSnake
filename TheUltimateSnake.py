#    _____  _                _   _  _  _    _                    _              _____                _          
#   |_   _|| |              | | | || || |  (_)                  | |            /  ___|              | |         
#     | |  | |__    ___     | | | || || |_  _  _ __ ___    __ _ | |_   ___     \ `--.  _ __    __ _ | | __  ___ 
#     | |  | '_ \  / _ \    | | | || || __|| || '_ ` _ \  / _` || __| / _ \     `--. \| '_ \  / _` || |/ / / _ \
#     | |  | | | ||  __/    | |_| || || |_ | || | | | | || (_| || |_ |  __/    /\__/ /| | | || (_| ||   < |  __/
#     \_/  |_| |_| \___|     \___/ |_| \__||_||_| |_| |_| \__,_| \__| \___|    \____/ |_| |_| \__,_||_|\_\ \___|
                                                                                                            
# Created by Campbell Lythe-Brown
# Techtorium Advanced Python | Project Nibbles Revamp
# Dated: 22/02/2021                                                                                                          


import pygame
import sys
import random
from pygame.math import Vector2


class Snake:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.snakeDirection = Vector2(1,0)
        self.newBlock = False

        self.headUp = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/head_up.png').convert_alpha()
        self.headDown = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/head_down.png').convert_alpha()
        self.headRight = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/head_right.png').convert_alpha()
        self.headLeft = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/head_left.png').convert_alpha()
		
        self.tailUp = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/tail_up.png').convert_alpha()
        self.tailDown = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/tail_down.png').convert_alpha()
        self.tailRight = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/tail_right.png').convert_alpha()
        self.tailLeft = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/tail_left.png').convert_alpha()

        self.bodyVertical = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/body_vertical.png').convert_alpha()
        self.bodyHorizontal = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/body_horizontal.png').convert_alpha()

        self.bodyTR = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/body_tr.png').convert_alpha()
        self.bodyTL = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/body_tl.png').convert_alpha()
        self.bodyBR = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/body_br.png').convert_alpha()
        self.bodyBL = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/body_bl.png').convert_alpha()
        self.crunchSound = pygame.mixer.Sound('C:/Users/campb/Documents/Tech/TheUltimateSnake/Sound/crunch.wav')

    def snakeReset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.snakeDirection = Vector2(1,0)
        self.newBlock = False
    
    def drawSnake(self):
        self.updateHeadGraphics()
        self.updateTailGraphics()

        for index,block in enumerate(self.body):
            xPosition = int(block.x * cellSize)
            yPosition = int(block.y * cellSize)
            blockRect = pygame.Rect(xPosition,yPosition,cellSize,cellSize)

            if index == 0:
                gameScreen.blit(self.head,blockRect)
            elif index == len(self.body) - 1:
                gameScreen.blit(self.tail,blockRect)
            else:
                previousBlock = self.body[index + 1] - block
                nextBlock = self.body[index - 1] - block
                if previousBlock.x == nextBlock.x:
                    gameScreen.blit(self.bodyVertical,blockRect)
                elif previousBlock.y == nextBlock.y:
                    gameScreen.blit(self.bodyHorizontal,blockRect)
                else:
                    if previousBlock.x == -1 and nextBlock.y == -1 or previousBlock.y == -1 and nextBlock.x == -1:
                        gameScreen.blit(self.bodyTL,blockRect)
                    if previousBlock.x == -1 and nextBlock.y == 1 or previousBlock.y == 1 and nextBlock.x == -1:
                        gameScreen.blit(self.bodyBL,blockRect)
                    if previousBlock.x == 1 and nextBlock.y == -1 or previousBlock.y == -1 and nextBlock.x == 1:
                        gameScreen.blit(self.bodyTR,blockRect)
                    if previousBlock.x == 1 and nextBlock.y == 1 or previousBlock.y == 1 and nextBlock.x == 1:
                        gameScreen.blit(self.bodyBR,blockRect)
                        
    def updateHeadGraphics(self):
        headRelation = self.body[1] - self.body[0]
        if headRelation == Vector2(1,0): self.head = self.headLeft
        elif headRelation == Vector2(-1,0): self.head = self.headRight
        elif headRelation == Vector2(0,1): self.head = self.headUp
        elif headRelation == Vector2(0,-1): self.head = self.headDown
    
    def updateTailGraphics(self):
        tailRelation = self.body[-2] - self.body[-1]
        if tailRelation == Vector2(1,0): self.tail = self.tailLeft
        elif tailRelation == Vector2(-1,0): self.tail = self.tailRight
        elif tailRelation == Vector2(0,1): self.tail = self.tailUp
        elif tailRelation == Vector2(0,-1): self.tail = self.tailDown



    def moveSnake(self):
        if self.newBlock == True:
            bodyCopy = self.body[:]
            bodyCopy.insert(0,bodyCopy[0] + self.snakeDirection)
            self.body = bodyCopy[:]
            self.newBlock = False
        else:
            bodyCopy = self.body[:-1]
            bodyCopy.insert(0,bodyCopy[0] + self.snakeDirection)
            self.body = bodyCopy[:]
    
    def addBlock(self):
        self.newBlock = True

class Fruit:
    def __init__(self):
        self.randomizePosition()
        

    def drawFruit(self):
        fruitRect = pygame.Rect(int(self.pos.x * cellSize),int(self.pos.y * cellSize),cellSize,cellSize)
        gameScreen.blit(gameApple,fruitRect)

    def randomizePosition(self):
        self.x = random.randint(0,cellNumber - 1)
        self.y = random.randint(0,cellNumber - 1)
        self.pos = Vector2(self.x,self.y)

class Main:
    global gameRunning
    global gameMenu
    global gameOver
    def __init__(self):
        self.gameSnake = Snake()
        self.gameFruit = Fruit()

    def updateGame(self):
        self.gameSnake.moveSnake()
        self.checkCollision()
        self.checkFail()

    def drawElements(self):
        self.drawGrass()
        self.gameFruit.drawFruit()
        self.gameSnake.drawSnake()
        self.drawScore()

    def checkCollision(self):
        if self.gameFruit.pos == self.gameSnake.body[0]:
            self.gameFruit.randomizePosition()
            self.gameSnake.addBlock()
    
    def gameOverNow(self):
        gameOver = True
        while gameOver:
            gameRunning = False
            gameScreen.fill((255,0,0))
            gameScreen.blit(gameOverScreen,(0,0)) 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE: 
                        gameRunning = True 
                        gameOver = False
                        gameMenu = False
                        self.gameSnake.snakeReset()

    def checkFail(self):
        if not 0 <= self.gameSnake.body[0].x < cellNumber or not 0 <= self.gameSnake.body[0].y < cellNumber:
            self.gameOverNow()

        for block in self.gameSnake.body[1:]:
            if block == self.gameSnake.body[0]:
                self.gameOverNow()

    def drawGrass(self):
        grassColor = (65,155,10)

        for row in range(cellNumber):
            if row % 2 == 0:
                for col in range(cellNumber):
                    if col % 2 == 0:
                        grassRect = pygame.Rect(col * cellSize,row * cellSize,cellSize,cellSize)
                        pygame.draw.rect(gameScreen,grassColor,grassRect)
            else:
                for col in range(cellNumber):
                    if col % 2 != 0:
                        grassRect = pygame.Rect(col * cellSize,row * cellSize,cellSize,cellSize)
                        pygame.draw.rect(gameScreen,grassColor,grassRect)
    
    def drawScore(self):
        scoreText = str(len(self.gameSnake.body) - 3)
        scoreSurface = gameFont.render(scoreText,True,(56,74,12))
        scoreX = int(cellSize * cellNumber - 60)
        scoreY = int(cellSize * cellNumber - 40)
        scoreRect = scoreSurface.get_rect(center = (scoreX,scoreY))
        gameScreen.blit(scoreSurface,scoreRect)

pygame.init()
pygame.font.init()
gameFont = pygame.font.Font('C:/Users/campb/Documents/Tech/TheUltimateSnake/Font/PoetsenOne-Regular.ttf',25)
cellSize = 40
cellNumber = 20
gameScreen = pygame.display.set_mode((cellNumber * cellSize,cellNumber * cellSize))
gameClock = pygame.time.Clock()
gameApple = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/apple.png').convert_alpha()
gameStartScreen = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/game_start.png')
gameOverScreen = pygame.image.load('C:/Users/campb/Documents/Tech/TheUltimateSnake/Graphics/game_over.png')
gameSpeed = 1
screenUpdate = pygame.USEREVENT
pygame.time.set_timer(screenUpdate,150)
mainGame = Main()

gameRunning = False
gameMenu = True
gameOver = False

while gameMenu:   
    gameScreen.fill((255,0,0))
    gameScreen.blit(gameStartScreen,(0,0)) 
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                gameRunning = True
                gameMenu = False
                gameOver = False
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == screenUpdate:
                mainGame.updateGame()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_UP:
                if mainGame.gameSnake.snakeDirection.y != 1:
                    mainGame.gameSnake.snakeDirection = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if mainGame.gameSnake.snakeDirection.y != -1:
                    mainGame.gameSnake.snakeDirection = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if mainGame.gameSnake.snakeDirection.x != 1:
                    mainGame.gameSnake.snakeDirection = Vector2(-1,0)
            if event.key == pygame.K_RIGHT:
                if mainGame.gameSnake.snakeDirection.x != -1:
                    mainGame.gameSnake.snakeDirection = Vector2(1,0)
    gameScreen.fill((65,152,10))
    mainGame.drawElements()
    gameClock.tick(60)
    pygame.display.update()  


     