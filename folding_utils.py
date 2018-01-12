import math
import itertools
from ComplexNumber import ComplexNumber


def get_coordinates(seq, conf):
    pass


def compute_free_energy(seq, pos):
    if len(pos) != len(set(pos)):
        raise ValueError
    pos_list = [pos[i] for i, x in enumerate(seq) if x == '1']
    energy = 0
    for comb in itertools.combinations(pos_list, 2):
        energy += distance(comb[0].re, comb[0].im, comb[1].re, comb[1].im)
    return energy


def read_from_file(file):
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f:
            yield line.split()


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
