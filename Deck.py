# The program that executes the main functions of the game.
# Author: Qifu Yin
# Date: 12-27-2018

from graphics import *
import random
import time
#from Deck import*
#from Button import*
#from Texts import*

class Deck:
    #This is a class for deck of playing card
    def __init__(self):
        self.suits = ['h', 's', 'd','c']
        #'h' represents heart, 's' represents spade, 'd' represent diamond, 'c' represents club
        self.number = ['1','2','3','4','5','6','7','8','9','10','j','q','k']

        #Create empty list
        self.deckcard = list()
        self.shuffledcard = list()

        for suit in self.suits:
            for num in self.number:
                card = suit + num
                self.deckcard.append(card)

    #Create methond to shuffle the deck
    def Shuffle(self):
        self.shuffledcard = self.deckcard
        random.shuffle(self.shuffledcard)
        return self.shuffledcard

    def deal(self):
        card = self.shuffledcard[0]##??
        return card

class Card(GraphicsObject):#subclass of GraphicsObject
    def __init__(self, win, value, center):
        self.value = value
        self.win = win
        self.center = center
        self.card = self.drawCard(value, center)
        self.card.draw(win)

    #Get the value of playing card
    def getvalue(self):
        if self.value[1] == 'j':
            value = 11
            return int(value)
        if self.value[1] == 'q':
            value = 12
            return int(value)
        if self.value[1] == 'k':
            value = 13
            return int(value)
        if slef.value[1:] == ['1','2','3','4','5','6','7','8','9','10']:
            value = self.value[1:]
            return int(value)

    #Get suit of playing card
    def getsuit(self):
        color = self.value[0]
        return color

    # def drawcard(self, value, center):
    #     self.center = center
    #     self.value = value
    #     file = 'draw_card'+str(value)+ '.gif'
    #     self.image = Image(center,file)
    #     return Image(center, file)
