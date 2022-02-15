from enum import Flag
import pygame

import tensorflow as tf

import sys
from PapatyaClasses import PapatyaModel
from PapatyaClasses import PapatyaLayer
from PapatyaClasses import PapatyaKernel

import pygame

def handleClick(frame, windows):
    mx, my = pygame.mouse.get_pos()
    for w in windows:
        if(w.visibility):
            for obj in w.objects:
                if(obj.x < mx and obj.x+obj.width > mx and obj.y < my and obj.y+obj.height > my and obj.isFocus):
                    obj.click()
                    return
            for obj in w.objects:
                obj.unclick()
            for obj in w.objects:
                if(obj.x < mx and obj.x+obj.width > mx and obj.y < my and obj.y+obj.height > my):
                    obj.click()
                    return
    for obj in frame.objects:
        if(obj.x < mx and obj.x+obj.width > mx and obj.y < my and obj.y+obj.height > my and obj.isFocus):
            obj.click()
            return
    for obj in frame.objects:
        obj.unclick()
    for obj in frame.objects:
        if(obj.x < mx and obj.x+obj.width > mx and obj.y < my and obj.y+obj.height > my):
            obj.click()
            return

def handleKeyDown(frame, windows, key):
    for w in windows:
        if(w.visibility):
            for obj in w.objects:
                if(obj.isFocus):
                    if(key.unicode == '\x08'):
                        obj.removeFromText()
                    else:
                        obj.appendToText(key.unicode)
    for obj in frame.objects:
        if(obj.isFocus):
            if(key.unicode == '\x08'):
                obj.removeFromText()
            else:
                obj.appendToText(key.unicode)

class ScreenObject:
    def __init__(self, name, x, y, frame):
        self.name = name
        self.x = frame.x+x
        self.y = frame.y+y
        self.frame = frame
        self.width = 0
        self.height = 0
        self.isFocus = False
    def blit(self):
        pass
    def click(self):
        pass
    def unclick(self):
        self.isFocus = False

class Button(ScreenObject):
    def __init__(self, name, x, y, frame, width, height, text):
        super().__init__(name, x, y, frame)
        self.width = width
        self.height = height
        self.text = text
        self.fontSize = 30
        self.function = None
    def blit(self, screen):
        font = pygame.font.Font("freesansbold.ttf",self.fontSize)
        pygame.draw.rect(screen, (150,150,230), (self.x, self.y, self.width, self.height))
        screen.blit(font.render(self.text, True, (50,50,50)), (self.x+5, self.y+5))
    def click(self):
        if(not self.function == None):
            self.function()

class EntryBox(ScreenObject):
    def __init__(self, name, x, y, frame, width, height):
        super().__init__(name, x, y, frame)
        self.width = width
        self.height = height
        self.fontSize = 30
        self.text = ""
        self.isFocus = False
    def blit(self, screen):
        if(self.isFocus):
            pygame.draw.rect(screen, (100,100,200), (self.x-2, self.y-2, self.width+4, self.height+4))
        font = pygame.font.Font("freesansbold.ttf", self.fontSize)
        pygame.draw.rect(screen, (220,220,220), (self.x, self.y, self.width, self.height))
        screen.blit(font.render(self.text, True, (15,15,15)), (self.x+5, self.y+5))
    def appendToText(self, ch):
        self.text+=ch
    def removeFromText(self):
        self.text=self.text[:-1]
    def click(self):
        self.isFocus = True

class SelectionMenu(ScreenObject):
    #TODO: isExtended is not required since we implement isFocus functionalit, remove isExtended.
    #TODO: There is no need to get width and height as argument since it is set as the size of item strings
    def __init__(self, name, x, y, frame, width, height, items):
        super().__init__(name, x, y, frame)
        self.items = items
        self.isExtended = False
        self.fontSize = 30
        self.selectedItem = None
        self.font = pygame.font.Font("freesansbold.ttf", self.fontSize)
        self.width , self.height = self.font.size(self.getLongestItem())
        self.width+=10
        self.height+=10
        self.itemHeight = self.height
    def blit(self, screen):
        if(self.isExtended):
            for i in range(len(self.items)):
                pygame.draw.rect(screen, (220,220,220), (self.x, self.y+i*self.itemHeight, self.width, self.itemHeight))
                screen.blit(self.font.render(self.items[i], True, (15,15,15)), (self.x+5, self.y+5+i*self.itemHeight))
        elif(self.selectedItem == None):
            pygame.draw.rect(screen, (220,220,220), (self.x, self.y, self.width, self.itemHeight))
            screen.blit(self.font.render(self.items[0], True, (15,15,15)), (self.x+5, self.y+5))
        else:
            pygame.draw.rect(screen, (220,220,220), (self.x, self.y, self.width, self.itemHeight))
            screen.blit(self.font.render(self.selectedItem, True, (15,15,15)), (self.x+5, self.y+5))
    def click(self):
        if(not self.isExtended):
            self.isFocus = True
            self.isExtended = True
            self.height = self.itemHeight*len(self.items)
        else:
            mx, my = pygame.mouse.get_pos()
            for i in range(len(self.items)):
                if(my > (self.y+self.itemHeight*i) and my < (self.y+self.itemHeight*(i+1))):
                    self.selectedItem = self.items[i]
                    self.isFocus = False
                    self.isExtended = False
                    self.height=self.itemHeight
    def unclick(self):
        if(self.isExtended):
            self.isFocus = False
            self.isExtended=False
            self.height=self.itemHeight
    # Private Functions
    def getLongestItem(self):
        maxLen = 0
        for i in self.items:
            if(len(i) > maxLen):
                longestItem = i
        return longestItem

class Node(ScreenObject):
    def __init__(self, name, x, y, frame, pl):
        super().__init__(name, x, y, frame)
        self.pLayer = pl #PapatyaLayer
        self.color = (150,150,150)
    def blit(self, screen, navigator_x, navigator_y):
        font = pygame.font.Font("freesansbold.ttf", 10)
        pygame.draw.rect(screen, self.color, (navigator_x+self.x, navigator_y+self.y, 50, 50))
        screen.blit(font.render(self.pl.name, True, (50, 50, 50), (navigator_x+self.x+5, navigator_y+self.y+5)))

class InputNode(Node):
    def __init__(self, name, x, y, frame, pl):
        super().__init__(name, x, y, frame, pl)
        self.color = (200,100,100)

class HiddenNode(Node):
    def __init__(self, name, x, y, frame, pl):
        super().__init__(name, x, y, frame, pl)

class OutputNode(Node):
    def __init__(self, name, x, y, frame, pl):
        super().__init__(name, x, y, frame, pl)
        self.color = (100,200,100)

class Frame:
    def __init__(self,title):
        self.title = title
        self.objects = []
        self.x = 0
        self.y = 0
    def blit(self, screen):
        for obj in self.objects:
            obj.blit(screen)
        for obj in self.objects:
            if(obj.isFocus):
                obj.blit(screen)
    def addObj(self, obj):
        self.objects.append(obj)

class Window(Frame):
    def __init__(self, title, width, height):
        super().__init__(title)
        self.width = width
        self.height = height
        self.x = (SCREEN_WIDTH-self.width)/2
        self.y = (SCREEN_HEIGHT-self.height)/2
        self.visibility = False
    def blit(self, screen):
        pygame.draw.rect(screen, (100,100,100), (self.x, self.y, self.width, self.height))
        super().blit(screen)

pygame.init()
SCREEN_WIDTH=1280
SCREEN_HEIGHT=720
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
isRun = True
FPS = 60
fpsClock = pygame.time.Clock()

# Creating main frame
mainFrame = Frame("main")
plusButton = Button("plusButton", 15, 720-65, mainFrame, 50, 50, "+")
mainFrame.addObj(plusButton)

currentFrame = mainFrame

# Creating new node window
windows = []

newNodeWindow = Window("New Node", 400, 200)
nodeType = SelectionMenu("nodeType", 50, 50, newNodeWindow, 300, 50, ["Input Layer", "HiddenLayer", "Output Layer"])
newNodeWindow.addObj(nodeType)
nameEntry = EntryBox("nameEntry", 50, 110, newNodeWindow, 300, 35)
newNodeWindow.addObj(nameEntry)
windows.append(newNodeWindow)

# Button functions
def mainFramePlusButtonFunc():
    newNodeWindow.visibility = True

plusButton.function = mainFramePlusButtonFunc

while(isRun):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            isRun = False
        if(event.type == pygame.MOUSEBUTTONDOWN):
            handleClick(currentFrame, windows)
        if(event.type == pygame.KEYDOWN):
            handleKeyDown(currentFrame, windows, event)

    screen.fill((50,50,50))
    currentFrame.blit(screen)

    for w in windows:
        if(w.visibility):
            w.blit(screen)

    pygame.display.flip()
    fpsClock.tick(FPS)
