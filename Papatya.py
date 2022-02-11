from enum import Flag
import pygame

import tensorflow as tf

import sys
sys.path.append(".")
from PapatyaClasses import PapatyaModel
from PapatyaClasses import PapatyaLayer
from PapatyaClasses import PapatyaKernel

import pygame

class ScreenObject:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def blit(self):
        pass

class Button(ScreenObject):
    def __init__(self, name, x, y, width, height, text):
        super().__init__(name, x, y)
        self.width = width
        self.height = height
        self.text = text
        self.fontSize = 30
    def blit(self, screen):
        font = pygame.font.Font("freesansbold.ttf",self.fontSize)
        pygame.draw.rect(screen, (150,150,230), self.x, self.y, self.width, self.height)
        screen.blit(font.render(self.text, True, (50,50,50)), (self.x+5, self.y+5))

class EntryBox(ScreenObject):
    def __init__(self, name, x, y, width, height):
        super().__init__(name, x, y)
        self.width = width
        self.height = height
        self.text = ""
    def blit(self, screen):
        pygame.draw.rect(screen, (220,220,220), self.x, self.y, self.width, self.height)
    def appendToText(self, ch):
        self.text+=ch

class Frame:
    def __init__(self,title):
        self.title = title
        self.objects = []
    def blit(self, screen):
        for obj in self.objects:
            obj.blit(screen)
    def addObj(self, obj):
        self.objects.append(obj)

pygame.init()
screen = pygame.display.set_mode((1280,720))
isRun = True
FPS = 60
fpsClock = pygame.time.Clock()
currentFrame = None

while(isRun):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            isRun = False
