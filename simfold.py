from itertools import accumulate
from ComplexNumber import ComplexNumber


def read_from_file(file):
    with open(file, 'rt', encoding='utf-8') as f:
        for line in f:
            yield line.split()


class BaseFolding:
    def __init__(self):
        self.folding = []

    def fold(self, file):
        for seq in read_from_file(file):
            self.folding.append(self.find_folding(seq))

    def find_folding(self, seq):
        pass

    def get_folding_list(self):
        return self.folding


class SpiralFolding(BaseFolding):
    def find_folding(self, seq):
        seq_len = len(seq)
        configuration = [None] * (seq_len - 1)
        conf = ComplexNumber(1, 0)
        turns = 0
        steps = 1
        step = 0
        for i in range(seq_len - 1):
            step += 1
            configuration[i] = str(conf)
            if step == steps:
                step = 0
                conf *= ComplexNumber(0, 1)
                turns += 1
                if turns % 2 == 0:
                    steps += 1
        return configuration


