from my_TK_original import *
import pygame
from colours import *
import main_shem
import simplify_2
from main_mine_schem import *


pygame.font.init()
font = pygame.font.Font('test_sans.ttf', 25)
SIZE = (900, 600)
CONST_SIZE = 0.7
SC = pygame.display.set_mode((SIZE[0], SIZE[1]), pygame.RESIZABLE)
CONST_SIZE_X, CONST_SIZE_Y = pygame.display.get_surface().get_size()
ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

ready1 = False
flag2 = True
flag3 = False
one_time_panel = True
bits = 0
str_finished = ''
name = ''

def def_pass():
    pass

def all_0():
    for i in range(1, len(inputs_list)):
        if inputs_list[i].get() == '':
            inputs_list[i].put('0')


def all_1():
    for i in range(1, len(inputs_list)):
        if inputs_list[i].get() == '':
            inputs_list[i].put('1')


def mine():
    global bits, str_finished, name
    main_fun(bits, str_finished, inputs_list[-1].get())



def simplify():
    global text_list, str_finished
    list_where_1 = []
    for i in range(1, len(inputs_list)):
        if inputs_list[i].get() == '0' or inputs_list[i].get() == '1':
            pass
        else:
            text2 = Text(SC, 'Поля заполнены некоретно (только 0 и 1)', DARK_GREEN, 25 * CONST_SIZE, 500 * CONST_SIZE, 250 * CONST_SIZE)
            text_list.append(text2)
            print('ПОЛЯ НЕ ЗАПОЛНЕНЫ')
            return

    for i in range(len(inputs_list)):
        if inputs_list[i].get() == '1':
            list_where_1.append(([i], '  '.join(bin(i-1)[2:].zfill(bits))))

    if list_where_1 != []:
        F_binary = simplify_2.Quine_McCluskey(list_where_1, bits)
        print('F-binary', F_binary)

        str_finished = ''
        for i in range(len(F_binary)):
            if i != 0:
                str_finished += ' + '
            comb_now = list(F_binary[i].replace('  ', ''))
            for j in range(len(comb_now)):
                if comb_now[j] != '*':
                    if comb_now[j] == '1':
                        str_finished += ALF[j]
                    else:
                        str_finished += '!' + ALF[j]
        text_list = []
        if str_finished == '':
            text2 = Text(SC, 'Все единицы', DARK_GREEN, 25 * CONST_SIZE, 500 * CONST_SIZE, 250 * CONST_SIZE)
            text_list.append(text2)
            print('Все единицы')
        else:
            text2 = Text(SC, 'ДНФ:    ' + str_finished, DARK_GREEN, 25, 500 * CONST_SIZE, 250 * CONST_SIZE)
            text_list.append(text2)
            print(str_finished)
            if bits >= 5:
                panel = Panel(SC, GREEN, 500 * CONST_SIZE, 400 * CONST_SIZE, (200 * CONST_SIZE * bits, 450 * CONST_SIZE), (200 * CONST_SIZE * bits, 40 * len(str_finished) * CONST_SIZE))
            else:
                panel = Panel(SC, GREEN, 500 * CONST_SIZE, 400 * CONST_SIZE, (750 * CONST_SIZE, 450 * CONST_SIZE), (750 * CONST_SIZE, 25 * len(str_finished) * CONST_SIZE))
            panels_list.append(panel)
            shem = main_shem.Shem(panels_list[-1].surf, bits, str_finished)
            text_list.append(shem)

            text2 = Text(SC, 'Конвертировать в схематик', DARK_GREEN, 25 * CONST_SIZE, 890 * CONST_SIZE, 20 * CONST_SIZE)
            text_list.append(text2)
            input = Input(SC, DARK_GREEN, DARK_GREEN, 870 * CONST_SIZE, 80 * CONST_SIZE, (250, 35), 'Название: ', 50, False, None)
            inputs_list.append(input)
            but = Button(SC, 'Конвертировать', DARK_GREEN, 24, DARK_GREEN, 870 * CONST_SIZE, 150 * CONST_SIZE, (250, 35), mine, False, None)
            buttons_list.append(but)


    else:
        text2 = Text(SC, 'Все нули', DARK_GREEN, 25 * CONST_SIZE, 500 * CONST_SIZE, 250 * CONST_SIZE)
        text_list.append(text2)
        print('Все нули')



def ready1_fun():
    global ready1, bits, flag3
    if inputs_list[0].get() != '':
        bits = int(inputs_list[0].get())
        if bits > 8:
            print("Нельзя больше 8")
            inputs_list[0].put("")
            text2 = Text(SC, 'Максимум 8 входов', DARK_GREEN, 25 * CONST_SIZE, 500 * CONST_SIZE, 250 * CONST_SIZE)
            text_list.append(text2)
            flag3 = True
        else:
            if flag3:
                text_list.pop()
            but = Button(SC, '+', DARK_GREEN, 24, DARK_GREEN, 800 * CONST_SIZE + 40, 50 * CONST_SIZE, (40 * CONST_SIZE, 40 * CONST_SIZE), ready1_fun, False, None)
            buttons_list.pop(0)
            buttons_list.append(but)
            ready1 = True


def wait1_buttons():
    global flag2
    if flag2:
        if ready1:
            flag2 = False
            return True
        else:
            return False


def tabel_input():
    global one_time_panel, bits
    if wait1_buttons():
        if one_time_panel:
            print(40 * 2**bits)
            if 40 * 2**bits > 319:
                panel = Panel(SC, DARK_GREEN, 50 * CONST_SIZE, 300 * CONST_SIZE, (350 * CONST_SIZE + 20, 450 * CONST_SIZE), (350 * CONST_SIZE + 20, 40 * 2**bits))
            else:
                panel = Panel(SC, DARK_GREEN, 50 * CONST_SIZE, 300 * CONST_SIZE, (350 * CONST_SIZE + 20, 200 * CONST_SIZE), (350 * CONST_SIZE + 20, 40 * 2 ** bits))
            panels_list.append(panel)
            i = 0
            while len(bin(i)[2:]) <= bits:
                input = Input(panels_list[0].surf, DARK_GREEN, DARK_GREEN, 10 * CONST_SIZE,  40 * i * CONST_SIZE, (33.333333 * bits + 40 * CONST_SIZE, 40 * CONST_SIZE), '  '.join(bin(i)[2:].zfill(bits)) + ' :    ', 1, True, panels_list[0])
                inputs_list.append(input)
                i += 1
            one_time_panel = False

            but = Button(SC, 'Заполнить всё 0', DARK_GREEN, 24, DARK_GREEN, 50 * CONST_SIZE, 50 * CONST_SIZE, (230 * CONST_SIZE + 40, 45 * CONST_SIZE), all_0, False, None)
            buttons_list.append(but)

            but = Button(SC, 'Заполнить всё 1', DARK_GREEN, 24, DARK_GREEN, 50 * CONST_SIZE, 100 * CONST_SIZE, (230 * CONST_SIZE + 40, 45 * CONST_SIZE), all_1, False, None)
            buttons_list.append(but)

            but = Button(SC, 'Упростить', DARK_GREEN, 24, DARK_GREEN, 50 * CONST_SIZE, 150 * CONST_SIZE, (230 * CONST_SIZE + 40, 45 * CONST_SIZE), simplify, False, None)
            buttons_list.append(but)
            buttons_list.pop(0)
    if wait1_buttons and flag2 == False:
        text1 = Text(SC, '   '.join(list(ALF[0:bits])) + '         Y', DARK_GREEN, 24 * CONST_SIZE, 67 * CONST_SIZE + 7, 270 * CONST_SIZE)
        text1.draw()
        pygame.draw.rect(SC, DARK_GREEN, (50 * CONST_SIZE, 265 * CONST_SIZE, 350 * CONST_SIZE + 20, 35 * CONST_SIZE + 20), 1)





def draw():
    SC.fill(BLACK)
    for j in panels_list:
        j.draw()
    SC.fill(BLACK)
    for j in buttons_list:
        j.draw()
    for j in inputs_list:
        j.draw()
    for j in text_list:
        j.draw()

input = Input(SC, DARK_GREEN, DARK_GREEN, 500 * CONST_SIZE, 50 * CONST_SIZE, (250 * CONST_SIZE + 40, 45 * CONST_SIZE), 'Сколько входов: ', 2, False, None)
inputs_list.append(input)
but = Button(SC, '', WHITE, 24, DARK_GREEN, 800 * CONST_SIZE + 40, 50 * CONST_SIZE, (40 * CONST_SIZE, 45 * CONST_SIZE), ready1_fun, False, None)


buttons_list.append(but)


while True:

    mainloop()

    draw()

    tabel_input()

    pygame.time.delay(50)
    pygame.display.update()