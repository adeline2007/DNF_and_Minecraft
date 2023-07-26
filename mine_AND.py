import pygame
from colours import *
pygame.font.init()
font = pygame.font.Font('test_sans.ttf', 25)
ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def make_bridge(x1, y1, x2, y2, z):
    help_ = []
    help_.append((6, x1, y1 - 1, z + 1, BLUE)) #повторитель внииз
    help_.append((1, x1 + 1, y1, z + 1, GRAY))
    help_.append((4, x1 + 1, y1, z + 2, RED))
    help_.append((1, x1 + 2, y1, z + 2, GRAY))
    help_.append((4, x1 + 2, y1, z + 3, RED))
    if x2-x1 > 4:
        for i in make_line(x1 + 3, y1, x2 - 2, y2, z + 3):
            help_.append(i)
    help_.append((1, x2 - 1, y1, z + 2, GRAY))
    help_.append((4, x2 - 1, y1, z + 3, RED))
    help_.append((1, x2, y1, z+1, GRAY))
    help_.append((4, x2, y1, z + 2, RED))
    return help_


def make_line(x1, y1, x2, y2, z, l=10):
    help_ = []
    cheak = 0
    if x1 == x2:
        while y1 <= y2:
            if cheak != l:
                help_.append((1, x1, y1, z, GRAY))  # 0 - кварцевый блок
                help_.append((4, x1, y1, z + 1, RED))  # redstone
                y1 += 1
                cheak += 1
            else:
                help_.append((1, x1, y1, z, GRAY))
                help_.append((6, x1, y1, z+1, BLUE)) #повторитель внииз
                cheak = 0
                y1 += 1
    elif y1 == y2:
        while x1 <= x2:
            if cheak != l:
                help_.append((1, x1, y1, z, GRAY))  # 0 - кварцевый блок
                help_.append((4, x1, y1, z + 1, RED))  # redstone
                x1 += 1
                cheak += 1
            else:
                help_.append((1, x1, y1, z, GRAY))
                help_.append((8, x1, y1, z+1, BLUE))  # повторитель вправо
                cheak = 0
                x1 += 1

    else:
        print("Эээ... тут у тебя все разные значения")
        return None
    return help_


class And:
    def __init__(self, bits, minterm, list_cor, x, y):
        self.bits = bits
        self.minterm = minterm
        self.list_cor = list_cor
        self.x = x
        self.y = y
        self.height = len(list(self.minterm.replace('!', ''))) * 2
        self.width = 6
        self.blocks = []
        self.list_cor_lastpoint = self.y + len(self.minterm.replace('!', '')) * 2

    def draw(self):
        count = len(list(self.minterm.replace('!', '')))
        self.height = count * 50
        k = self.y
        for i in range(count):
            kek = make_bridge(self.list_cor[ALF.find(list(self.minterm.replace('!', ''))[i])], k, 18, k, 0)
            k += 2
            for j in kek:
                self.blocks.append(j)


        for i in range(len(self.minterm.replace('!', ''))):
            list_no = self.minterm.replace('', '%').replace('!%', '!').split('%')
            list_no.pop(-1)
            list_no.pop(0)
            if '!' in list_no[i]:
                self.blocks.append((1, 19, self.y + i * 2, 2, GRAY))
                self.blocks.append((3, 20, self.y + i * 2, 2, DARK_RED)) #факел для НЕ
                self.blocks.append((1, 21, self.y + i * 2, 1, GRAY))
                self.blocks.append((4, 21, self.y + i * 2, 2, RED))
            else:
                self.blocks.append((1, 19, self.y + i * 2, 1, GRAY))
                self.blocks.append((8, 19, self.y + i * 2, 2, BLUE))
                self.blocks.append((1, 20, self.y + i * 2, 1, GRAY))
                self.blocks.append((4, 20, self.y + i * 2, 2, RED)) #редстоун
                self.blocks.append((1, 21, self.y + i * 2, 1, GRAY))
                self.blocks.append((4, 21, self.y + i * 2, 2, RED))

        for i in range(len(self.minterm.replace('!', '')) * 2 - 1):
            self.blocks.append((1, 22, self.y + i, 2, GRAY))
            self.blocks.append((1, 23, self.y + i, 2, GRAY))
            self.blocks.append((4, 23, self.y + i, 3, RED))
            if i % 2 == 0:
                self.blocks.append((7, 22, self.y + i, 3, DARK_RED)) #факел
        self.blocks.append((3, 24, self.y + (len(self.minterm.replace('!', '')) * 2 - 1) // 2, 2, DARK_RED))
        return self.blocks
