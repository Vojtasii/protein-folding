import turtle
from fold import fold

def display(file):
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f:
            l = list(line.split())
            for i in l:
                if i == '1':
                    print('*', end=' ')
                else:
                    print('o', end=' ')
            print('\n')

if __name__ == '__main__':
    display('sequences_public.txt')