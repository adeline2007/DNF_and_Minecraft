import pygame
from colours import *
from pygame.locals import *
import sys
import win32api

text_list = []
inputs_list = []
buttons_list = []
panels_list = []
english_alf = 'qwertyuiopasdfghjklzxcvbnm'
russion_alf = 'йцукенгшщзфывапролдячсмить'
full_russion_alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
shift_eng = '~!@#$%^&*()_+{}:"|<>?'
shift_rus = 'ё!"№;%:?*()_+ХЪЖЭ/БЮ,'


import pygame as pg

class Text:
    def __init__(self, SC1, text, text_color, font, x, y):
        self.SC1 = SC1
        self.text = text
        self.text_color = text_color
        self.font = int(font)
        self.x = x
        self.y = y

    def draw(self):
        font1 = pygame.font.Font('cambria.ttc', self.font)
        text1 = font1.render(self.text, False, self.text_color)
        self.SC1.blit(text1, (self.x, self.y))


class Button:
    def __init__(self, SC1, text, text_color, font, color_button, x, y, size, test_funk, in_panel, panel):
        self.SC1 = SC1
        self.text = Text(self.SC1, text, text_color, font, x + 5, y+2)
        self.color_button = color_button
        self.x = x
        self.y = y
        self.size = size
        self.test_funk = test_funk
        self.in_panel = in_panel
        if self.in_panel:
            self.panel = panel

    def draw(self):
        if self.in_panel:
            pygame.draw.rect(self.SC1, self.color_button, (self.x, self.y, self.size[0], self.size[1]), 1)
            self.text.draw()
        else:
            pygame.draw.rect(self.SC1, self.color_button, (self.x, self.y, self.size[0], self.size[1]), 1)
            self.text.draw()

    def cheak(self, pos):
        if self.in_panel:
            if pos[0] < self.x + self.size[0] + self.panel.x and pos[0] > self.x + self.panel.x and pos[1] < self.y + self.size[1] + self.panel.y_bar and pos[1] > self.y + self.panel.y_bar:
                if pos[0] < self.panel.x + self.panel.size[0] and pos[0] > self.panel.x and pos[1] < self.panel.y + self.panel.size[1] and pos[1] > self.panel.y:
                    pygame.draw.rect(self.SC1, self.color_button, (self.x, self.y, self.size[0], self.size[1]), 1)
                    pygame.display.update()
                    pygame.time.delay(50)
                    self.test_funk()
        else:
            if pos[0] < self.x + self.size[0] and pos[0] > self.x and pos[1] < self.y + self.size[1] and pos[1] > self.y:
                pygame.draw.rect(self.SC1, self.color_button, (self.x, self.y, self.size[0], self.size[1]), 1)
                pygame.display.update()
                pygame.time.delay(50)
                self.test_funk()


class Input:
    def __init__(self, SC1, collorPole, collorText, x, y, size, Q, max_str, in_panel, panel):
        self.SC1 = SC1
        self.collorPole = collorPole
        self.collorText = collorText
        self.x = x
        self.y = y
        self.size = size
        self.Q = Q
        self.text = ''
        self.text_draw = Text(self.SC1, self.Q + self.text, self.collorText, 12, self.x + 7, self.y -2)
        self.work = False
        self.help_work = 0
        self.bukva = ''
        self.max_str = max_str
        self.one_time = True
        self.one_time2 = True
        self.in_panel = in_panel
        if self.in_panel:
            self.panel = panel

    def draw(self):
        pygame.draw.rect(self.SC1, self.collorPole, (self.x, self.y, self.size[0], self.size[1]), 1)
        if self.work:
            if self.one_time:
                self.text += '|'
                self.one_time = False
            if self.bukva == '':
                self.help_work += 1
                if self.help_work == 1:
                    if self.one_time2:
                        self.text = self.text[0:-1]
                        self.help_work = 0
                        self.one_time2 = False
                    else:
                        self.text += '|'
                if self.help_work == 50:
                    help1 = list(self.text)
                    help1.insert(0, 5)
                    if help1[-1] == '|':
                        self.text = self.text[0:-1]
                    self.help_work = 0
            else:
                help1 = list(self.text)
                help1.insert(0, 5)
                if self.text == '|':
                    self.text = ''
                elif help1[-1] == '|':
                    self.text = self.text[0:-1]

            if len(list(self.text)) < self.max_str:

                self.text += self.bukva
                self.bukva = ''
        else:
            help1 = list(self.text)
            help1.insert(0, 5)
            if self.text == '|':
                self.text = ''
            elif help1[-1] == '|':
                self.text = self.text[0:-1]
            self.help_work = 0

        self.text_draw = Text(self.SC1, self.Q + self.text, self.collorText, 24, self.x + 8, self.y -1)
        self.text_draw.draw()

    def cheak(self, pos):
        if self.in_panel:
            if pos[0] < self.x + self.size[0] + self.panel.x and pos[0] > self.x + self.panel.x and pos[1] < self.y + self.size[1] + self.panel.y_bar and pos[1] > self.y + self.panel.y_bar:
                if pos[0] < self.panel.x + self.panel.size[0] and pos[0] > self.panel.x and pos[1] < self.panel.y + self.panel.size[1] and pos[1] > self.panel.y:
                    self.work = True
                    return True
        else:
            if pos[0] < self.x + self.size[0] and pos[0] > self.x and pos[1] < self.y + self.size[1] and pos[1] > self.y:
                self.work = True
                return True
        return False

    def put(self, something):
        self.text = something

    def get(self):
        help1 = list(self.text)
        help1.insert(0, 5)
        if help1[-1] == '|':
            return self.text[0:-1]
        else:
            return self.text


class Panel:
    def __init__(self, SC1, collorPole, x, y, size, size_in):
        self.SC1 = SC1
        self.collorPole = collorPole
        self.x = x
        self.y = y
        self.y_bar = self.y
        self.y_scroll = self.y
        self.size = (size[0] - 15, size[1])
        self.size_in = (size_in[0] - 15, size_in[1])
        self.surf = pygame.Surface((self.size_in[0], self.size_in[1] + self.size[1]))
        self.last_mouse_y = 0
        self.scroll_work = False

    def draw(self):
        self.SC1.blit(self.surf, (self.x, self.y_bar))
        self.surf.fill(BLACK)
        #pygame.draw.rect(self.SC1, BLACK, (self.x, self.y, self.size[0], self.size[1]))
        pygame.draw.rect(self.SC1, DARK_GREEN, (self.x, self.y, self.size[0], self.size[1]), 1)
        pygame.draw.rect(self.SC1, DARK_GREEN, (self.x + self.size[0], self.y, 15, self.size[1]), 1)
        pygame.draw.rect(self.SC1, DARK_GREEN, (self.x + self.size[0] + 5, self.y_scroll, 5, self.size[1] / self.size_in[1] * self.size[1]))
        pygame.display.update((self.x, self.y), (self.size[0] + 15, self.size[1]))

    def cheak(self, pos):
        if pos[0] > self.x + self.size[0] + 5 and pos[0] < self.x + self.size[0] + 10 and pos[1] > self.y_scroll and pos[1] < self.y_scroll + self.size[1] / self.size_in[1] * self.size[1]:
            self.scroll_work = True
        else:
            self.scroll_work = False

    def scroll(self, pos):
        if self.scroll_work:
            if pos[1] + self.size[1] / self.size_in[1] * self.size[1] / 2 >= self.y + self.size[1]:
                self.y_scroll = self.y + self.size[1] - self.size[1] / self.size_in[1]  * self.size[1] -1
                self.y_bar = self.y - self.size_in[1]
            elif pos[1] - self.size[1] / self.size_in[1] * self.size[1] / 2 <= self.y:
                self.y_scroll = self.y+1
                self.y_bar = self.y
            else:
                self.y_scroll = pos[1] - self.size[1] / self.size_in[1] * self.size[1] / 2
                self.y_bar = self.y + (self.size_in[1] / (self.size[1] - self.size[1] / self.size_in[1] * self.size[1] -1)) * (self.y - self.y_scroll)
                #self.y_bar = (self.size_in[1] * (self.size_in[1] - pos[1])) / self.size[1] - self.y


def mainloop():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            for j in inputs_list:
                if j.work:
                    if i.key == pygame.K_BACKSPACE:
                        if j.text != '' and j.text != '|':
                            if j.text[-1] == '|':
                                j.text = j.text[0:-2]
                            else:
                                j.text = j.text[0:-1]
                    else:
                        if i.key < 1114111:
                            if win32api.GetKeyboardLayout() == 68748313:
                                if english_alf.find(chr(i.key)) == -1:
                                    j.bukva = chr(i.key)
                                else:
                                    j.bukva = russion_alf[english_alf.find(chr(i.key))]

                            else:
                                j.bukva = chr(i.key)
        if i.type == 1025:
            if i.button == 1:
                for j in buttons_list:
                    j.cheak(i.pos)
                for j in panels_list:
                        j.cheak(i.pos)
                for j in inputs_list:
                    if j.cheak(i.pos) == False and j.work == True:
                        j.work = False
                        j.one_time = True
                        j.one_time2 = True

        if i.type == 1026:
            for j in panels_list:
                if j.scroll_work:
                    j.scroll_work = False

        for j in panels_list:
            j.scroll(pygame.mouse.get_pos())