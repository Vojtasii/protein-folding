import math
from itertools import accumulate


SEQ_DIR = 'sequences_public.txt'
CONF_DIR = 'folding.txt'


def get_coordinates(seq, conf):
    pass


def compute_free_energy(seq, pos):
    pass


def read_from_file(file):
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f:
            yield line.split()


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


if __name__ == '__main__':
    for s, c in zip(read_from_file(SEQ_DIR), read_from_file(CONF_DIR)):
        p = [0]
        p.extend(accumulate(c))
        print(p)

