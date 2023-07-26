from colours import *
from mine_AND import And
import copy
import gzip
ALF = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
list_3d = []

def chunked(data, num):
    lst = []
    for i in range(0, len(data), num):
        lst.append(data[i:i+num])
    return lst


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
    help_.append((1, x2 - 1, y1, z + 1, GRAY))
    help_.append((4, x2 - 1, y1, z + 2, RED))
    help_.append((1, x2, y1, z, GRAY))
    help_.append((4, x2, y1, z + 1, RED))
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


def append_block(block, x, y, z):
    global list_3d
    print(block, x, y, z)
    list_3d[z][y][x] = copy.deepcopy(block)


class Shem:
    def __init__(self, bits, function):
        self.bits = bits
        self.function = function
        self.minterm_list = function.split(' + ')
        self.list_and = []
        self.cor = []
        self.blocks = []

    def draw(self):
        if self.bits != 0:
            for i in range(self.bits):
                self.cor.append(i*2)

        if self.function != 'ERROR888':
            self.list_and.append(And(self.bits, self.minterm_list[0], self.cor, 18, 2))
            for i in range(1, len(self.minterm_list)):
                self.list_and.append(And(self.bits, self.minterm_list[i], self.cor, 18, self.list_and[i-1].list_cor_lastpoint))

        for i in self.list_and:
            for j in i.draw():
                self.blocks.append(j)

        return self.blocks



def main_fun(bits, shem, name):
    global list_3d
    shem = Shem(bits, shem) #______________________________________________

    blocks = shem.draw()
    max_l = 0
    for i in blocks:
        if i[2] > max_l:
            max_l = i[2]
    print(max_l)
    for i in range(6):
        help_ = []
        for j in range(max_l+1):
            help_.append(['0']*26)
        list_3d.append(help_)

    for i in range(bits):
        blocks.append((1, i * 2, 0, 0, GRAY)) #кварц
        blocks.append((5, i * 2, 0, 1, LIGHT_BLUE)) #на нём рычаг
        blocks.append((1, i * 2, 1, 0, GRAY))  # кварц
        blocks.append((6, i * 2, 1, 1, BLUE)) #повторитель вниз
        for j in make_line(i * 2, 2, i * 2, max_l, 0, 15):
            blocks.append(j)

    blocks = shem.draw()
    cheak = 0
    y1 = 0
    while y1 <= max_l:
        if cheak != 15:
            blocks.append((1, 25, y1, 1, GRAY))  # 0 - кварцевый блок
            blocks.append((4, 25, y1, 2, RED))  # redstone
            y1 += 1
            cheak += 1
        else:
            blocks.append((1, 25, y1, 1, GRAY))
            blocks.append((6, 25, y1, 2, BLUE))  # повторитель вправо
            cheak = 0
            y1 += 1


    for i in blocks:
        print(i)
        append_block(str(i[0]), i[1], i[2], i[3])

    print("width", len(list_3d[0][0]))
    print("length", len(list_3d[0]))
    print("height", len(list_3d))

    k = hex(len(list_3d[0][0]))[2:]
    k = "0000"[:4 - len(k)] + k
    width = ' '.join(chunked(k, 2))

    k = hex(len(list_3d[0]))[2:]
    k = "0000"[:4 - len(k)] + k
    length = ' '.join(chunked(k, 2))

    k = hex(len(list_3d))[2:]
    k = "0000"[:4 - len(k)] + k
    height = ' '.join(chunked(k, 2))

    print(width)
    print(length)
    print(height)

    k = hex(len(list_3d[0][0]) * len(list_3d[0]) * len(list_3d))[2:]
    k = "00000000"[:8 - len(k)] + k
    size = ' '.join(chunked(k, 2))
    print(size)



    start_str = f"0A 00 09 53 63 68 65 6D 61 74 69 63 03 00 0A 50 61 6C 65 74 74 65 4D 61 78 00 00 00 08 0A 00 07 50 61 6C 65 74 74 65 03 00 22 6D 69 6E 65 63 72 61 66 74 3A 72 65 64 73 74 6F 6E 65 5F 74 6F 72 63 68 5B 6C 69 74 3D 74 72 75 65 5D 00 00 00 07 03 00 17 6D 69 6E 65 63 72 61 66 74 3A 73 6D 6F 6F 74 68 5F 71 75 61 72 74 7A 00 00 00 01 03 00 43 6D 69 6E 65 63 72 61 66 74 3A 72 65 70 65 61 74 65 72 5B 64 65 6C 61 79 3D 31 2C 66 61 63 69 6E 67 3D 6E 6F 72 74 68 2C 6C 6F 63 6B 65 64 3D 66 61 6C 73 65 2C 70 6F 77 65 72 65 64 3D 66 61 6C 73 65 5D 00 00 00 06 03 00 0D 6D 69 6E 65 63 72 61 66 74 3A 61 69 72 00 00 00 00 03 00 4A 6D 69 6E 65 63 72 61 66 74 3A 72 65 64 73 74 6F 6E 65 5F 77 69 72 65 5B 65 61 73 74 3D 6E 6F 6E 65 2C 6E 6F 72 74 68 3D 73 69 64 65 2C 70 6F 77 65 72 3D 30 2C 73 6F 75 74 68 3D 73 69 64 65 2C 77 65 73 74 3D 6E 6F 6E 65 5D 00 00 00 04 03 00 33 6D 69 6E 65 63 72 61 66 74 3A 72 65 64 73 74 6F 6E 65 5F 77 61 6C 6C 5F 74 6F 72 63 68 5B 66 61 63 69 6E 67 3D 65 61 73 74 2C 6C 69 74 3D 74 72 75 65 5D 00 00 00 03 03 00 36 6D 69 6E 65 63 72 61 66 74 3A 6C 65 76 65 72 5B 66 61 63 65 3D 66 6C 6F 6F 72 2C 66 61 63 69 6E 67 3D 6E 6F 72 74 68 2C 70 6F 77 65 72 65 64 3D 66 61 6C 73 65 5D 00 00 00 05 03 00 42 6D 69 6E 65 63 72 61 66 74 3A 72 65 70 65 61 74 65 72 5B 64 65 6C 61 79 3D 31 2C 66 61 63 69 6E 67 3D 77 65 73 74 2C 6C 6F 63 6B 65 64 3D 66 61 6C 73 65 2C 70 6F 77 65 72 65 64 3D 66 61 6C 73 65 5D 00 00 00 08 00 03 00 07 56 65 72 73 69 6F 6E 00 00 00 02 02 00 06 4C 65 6E 67 74 68 {length} 0A 00 08 4D 65 74 61 64 61 74 61 03 00 09 57 45 4F 66 66 73 65 74 58 00 00 00 01 03 00 09 57 45 4F 66 66 73 65 74 59 00 00 00 00 03 00 09 57 45 4F 66 66 73 65 74 5A FF FF FF F2 00 02 00 06 48 65 69 67 68 74 {height} 03 00 0B 44 61 74 61 56 65 72 73 69 6F 6E 00 00 0B 9F 07 00 09 42 6C 6F 63 6B 44 61 74 61 {size}"
    last_str = f"09 00 0D 42 6C 6F 63 6B 45 6E 74 69 74 69 65 73 0A 00 00 00 00 02 00 05 57 69 64 74 68 {width} 0B 00 06 4F 66 66 73 65 74 00 00 00 03 00 00 01 54 00 00 00 04 FF FF FE A4 00"
    str_mid = ""
    test_str = ""

    list_new = list(str(list_3d).replace('[', '').replace(']', '').replace(',', '').replace(' ', '').replace("'", ""))
    for i in list_new:
        str_mid += '0' + i + ' '
        test_str += i + ' '

    print(str_mid)
    print(test_str)
    main_str = start_str + ' '  + str_mid[:-1] + ' ' + last_str
    print(main_str)

    save_in = r"C:\Users\Пользователь\AppData\Roaming\.minecraft\config\worldedit\schematics"

    with gzip.open(f'{save_in}\{name}.schem', 'wb') as f:
        f.write(bytes([int(i, 16) for i in main_str.split(" ")]))










