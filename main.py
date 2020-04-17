"""Project-Case: TurnFuel
   Developers: Silkachev Vinnikov Popov"""
d1 = {'turn': '', 'time_start': '', 'time_end': ''}
d2 = {'turn': '', 'time_start': '', 'time_end': ''}
d3 = {'turn': '', 'time_start': '', 'time_end': ''}

with open('azs.txt', 'r') as s:
    b = s.readlines()
    azs1 = str(b[0][2:]).replace('\n','').split(' ')
    azs2 = (b[1][2:]).split()
    azs3 = (b[2][2:]).split()
    turn1 = int(azs1[0])
    turn2 = int(azs2[0])
    turn3 = int(azs3[0])
k1 = k2 = k3 = 0
print(azs1)

def main():
    with open('input.txt', 'r') as f:
        a = f.readlines()
        for line in a:
            chose_column(line,turn1, turn2, turn3, azs1, azs2, azs3)
            #print(str(line).replace('\n','').split(' '))
    pass


def chose_column(line,turn1, turn2, turn3, azs1, azs2, azs3):  # Выбор колонки, составление словаря тут.
    if turn1 > turn2 and set(azs1) & set(str(line).replace('\n','').split(' ')) and len(d1['turn']) < int(turn1):
        d1['turn'] += '*'
        d1['time_start'] = line[:5]
        turn1 -= len(d1['turn'])
        print(d1)
    else:
        print(str(line).replace('\n','').split(' '), azs1)


def time():  # Хз надо ли, можно просто в мэйн пихнуть, считает время.
    pass


def print_():  # Выводит хрень мол кто куда встал и насколько что занято.
    pass


main()
