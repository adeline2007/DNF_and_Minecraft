bits = 0
i = 0
list_count = []
list_data = []
list_new1 = []
alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def sort_for_count_1(list_):
    list_finished = []
    #list_help = []
    count_one = 0
    for i in range(bits+1):
        for j in range(len(list_)):
            if list_[j][1].count('1') == count_one:
                list_finished.append(list_[j])
        #list_finished.append(list_help)
        #list_help = []
        count_one += 1
    return list_finished


def sort_for_star_second(list_):
    list_finished = []
    list_asociations = [0]*len(list_)
    for i in range(len(list_)):
        for j in range(len(list_)):
            #print(i, j)
            if i != j:
                otl = 0
                id_otl = 0
                count_for_finish = list(list_[i][1].replace('  ', ''))
                number_strs = []
                for k in range(bits):
                    if list(list_[i][1].replace('  ', ''))[k] != list(list_[j][1].replace('  ', ''))[k]:
                        otl += 1
                        id_otl = k

                if otl == 1:
                    list_asociations[i] += 1
                    list_asociations[j] += 1
                    #print('list_', list_asociations)
                    count_for_finish[id_otl] = '*'

                    for l in range(len(list_[i][0])):
                        number_strs.append(list_[i][0][l])
                    for l in range(len(list_[j][0])):
                        number_strs.append(list_[j][0][l])

                    list_finished.append([number_strs, '  '.join(count_for_finish)])
    for i in range(len(list_asociations)):
        if list_asociations[i] == 0:
            list_finished.append(list_[i])
    return list_finished


def my_set(list_):
    list_set = []
    finished_list = []
    for i in range(len(list_)):
        if list_[i][1] not in list_set:
            list_set.append(list_[i][1])
    for i in range(len(list_set)):
        times = 0
        id_numbers = []
        for j in range(len(list_)):
            if list_set[i] == list_[j][1] and times == 0:
                times += 1
                id_numbers = list_[j][0]
        finished_list.append([id_numbers, list_set[i]])
    return finished_list


def redundancy(list_):
    finished_list = []
    for i in range(len(list_)-1):
        now_list = list_[i][0]
        found = set()
        for j in range(len(now_list)):
            for k in range(len(list_)):
                if list_[k][0] != 'STOP' and now_list[j] != 'STOP' and list_[i] != list_[k]:
                    now = now_list[j]
                    next = list_[k][0]
                    if now_list[j] in next:
                        found.add(now)
                        break
        if sorted(list(found)) == sorted(now_list):
            list_[i][0] = 'STOP'
    for i in range(len(list_)):
        if list_[i][0] != 'STOP':
            finished_list.append(list_[i][1])
    return finished_list


def Quine_McCluskey(list_, bit):
    global bits
    i = 0
    if i == 0:
        bits = bit
    i += 1
    list_ = sort_for_count_1(list_)
    #print(list_)
    for i in range(bits):
        list_ = sort_for_star_second(list_)
        #print(list_)
        list_ = my_set(list_)
        #print(list_)
    list_ = redundancy(list_)
    return list_
