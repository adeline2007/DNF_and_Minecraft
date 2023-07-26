import pygame
from colours import *
from AND import And
font = pygame.font.Font('test_sans.ttf', 25)
ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



class Shem:
    def __init__(self, SC1, bits, function):
        self.SC1 = SC1
        self.bits = bits
        self.function = function
        self.minterm_list = (function.replace(' + ', '$')).split('$')
        self.list_and = []
        print('kek', self.minterm_list)
        self.cor = []

    def draw(self):
        if self.bits != 0:
            for i in range(self.bits):
                pygame.draw.line(self.SC1, DARK_GREEN, (25 + 30 * i, 50), (25 + 30 * i, 10000), 3)
                self.cor.append(25 + 30 * i)
                text1 = font.render(ALF[i], False, DARK_GREEN)
                self.SC1.blit(text1, (17 + 30 * i, 25))

        if self.function != 'ERROR888':
            self.list_and.append(And(self.SC1, self.bits, self.minterm_list[0], self.cor, 66.6 * self.bits, 100))
            for i in range(1, len(self.minterm_list)):
                self.list_and.append(And(self.SC1, self.bits, self.minterm_list[i], self.cor, 66.6 * self.bits, self.list_and[i-1].height + self.list_and[i-1].y))

        for i in self.list_and:
            i.draw()

        corx = self.list_and[0].list_cor_lastpoint[0][0]
        cory = (self.list_and[0].list_cor_lastpoint[0][1] + self.list_and[-1].list_cor_lastpoint[0][1]) / 2
        pygame.draw.line(self.SC1, DARK_GREEN, self.list_and[0].list_cor_lastpoint[0], self.list_and[-1].list_cor_lastpoint[0], 3)
        pygame.draw.line(self.SC1, DARK_GREEN, (corx, cory), (corx+100, cory), 3)