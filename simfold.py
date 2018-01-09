from itertools import accumulate
from ComplexNumber import ComplexNumber
from folding_utils import read_from_file

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
        left_turn = ComplexNumber(0, 1)
        turns = 0
        steps = 1
        step = 0
        for i in range(seq_len - 1):
            step += 1
            configuration[i] = conf
            if step == steps:
                step = 0
                conf *= left_turn
                turns += 1
                if turns % 2 == 0:
                    steps += 1
        return configuration

