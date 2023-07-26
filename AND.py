import pygame
from colours import *
pygame.font.init()
font = pygame.font.Font('test_sans.ttf', 25)
ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def AND(minterm, x, y):
    count = len(list(minterm.replace('!', '')))
    height = count * 25
    width = 100
    for i in range(count):
        pygame.draw.line(SC, DARK_GREEN, (x, y + 25*i), (x + width, y + 25*i), 3)
    pygame.draw.rect(SC, DARK_GREEN, (x + width / 2, y, width / 2, height - 25), 3)

    pygame.draw.line(SC, DARK_GREEN, (x + width, y + height / 2 - 15), (x + width + 50, y + height / 2 - 15), 3)
    text1 = font.render('&', False, DARK_GREEN)
    SC.blit(text1, (width + x - width / 3, y + height / 2 - 25))


class And:
    def __init__(self, SC, bits, minterm, list_cor, x, y):
        self.SC = SC
        self.bits = bits
        self.minterm = minterm
        self.list_cor = list_cor
        self.list_cor_lastpoint = []
        self.x = x
        self.y = y
        self.height = len(list(self.minterm.replace('!', ''))) * 50
        self.width = 100

    def draw(self):
        count = len(list(self.minterm.replace('!', '')))
        self.height = count * 50
        for i in range(count):
            pygame.draw.line(self.SC, DARK_GREEN, (self.list_cor[ALF.find(list(self.minterm.replace('!', ''))[i])], self.y + 50 * i), (self.x + self.width, self.y + 50 * i), 3)
            pygame.draw.rect(self.SC, DARK_GREEN, (self.list_cor[ALF.find(list(self.minterm.replace('!', ''))[i])] - 5 , self.y + 50 * i - 5, 10, 10))
        pygame.draw.rect(self.SC, DARK_GREEN, (self.x + self.width / 2, self.y, self.width / 2, self.height - 50), 3)
        pygame.draw.line(self.SC, DARK_GREEN, (self.x + self.width, self.y + self.height / 2 - 25), (self.x + self.width + 50, self.y + self.height / 2 - 25), 3)
        self.list_cor_lastpoint.append((self.x + self.width + 50, self.y + self.height / 2 - 25))
        text1 = font.render('&', False, DARK_GREEN)
        if count > 1:
            self.SC.blit(text1, (self.width + self.x - self.width / 3, self.y + self.height / 2 - 37))


        for i in range(len(self.minterm.replace('!', ''))):
            list_no = self.minterm.replace('', '%').replace('!%', '!').split('%')
            list_no.pop(-1)
            list_no.pop(0)
            if '!' in list_no[i]:
                pygame.draw.rect(self.SC, BLACK, (50 * self.bits, self.y + 50 * i - 12.5, 25, 25))
                pygame.draw.rect(self.SC, DARK_GREEN, (50 * self.bits, self.y + 50 * i - 12.5, 25, 25), 2)
                text1 = font.render('1', False, DARK_GREEN)
                self.SC.blit(text1, (51.6 * self.bits, self.y + 50 * i - 12.5))
