import math
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
        return [1] * (len(seq) - 1)

    def get_folding_list(self):
        return self.folding


class SpiralFolding(BaseFolding):
    def find_folding(self, seq):
        seq_len = len(seq)
        configuration = [None] * (seq_len - 1)
        conf = ComplexNumber(1, 0)
        left_turn = ComplexNumber(0, 1)
        increase = False
        steps = 1
        step = 0
        for i in range(seq_len - 1):
            step += 1
            configuration[i] = conf
            if step == steps:
                step = 0
                conf *= left_turn
                if increase:
                    steps += 1
                    increase = False
                else:
                    increase = True

        return configuration


class RandomFolding(BaseFolding):
    def find_folding(self, seq):
        pass


class BedSheetFolding(BaseFolding):
    def find_folding(self, seq):
        seq_len = len(seq)
        seq_parts = self.separate_seq_into_parts(seq)
        #print(seq_parts, seq_len)
        configuration = self.fold_sheet(seq_parts, math.ceil(math.sqrt(seq_len-seq_parts[0])), seq_len)
        return configuration

    @staticmethod
    def fold_sheet(parts, row, length):
        # indices = [s for s in accumulate(parts)]
        configuration = [ComplexNumber(1, 0)] * (length - 1)
        conf = ComplexNumber(0, 1)
        skip = parts[0]
        iter_parts = iter(parts)
        next(iter_parts)
        color = 1
        i = 0
        step = 0
        for part in iter_parts:
            if color:
                overhang = part + step - row
                while overhang > 0:
                    configuration[skip + i + row - step - 1] *= conf
                    overhang -= row - step
                    step = 0

            if (i + 1) % row == 0:
                configuration[skip + i] *= conf
                configuration = [c * ComplexNumber(-1, 0) if s > skip + i else c for s, c in enumerate(configuration)]
                conf *= ComplexNumber(-1, 0)
        return configuration


    @staticmethod
    def separate_seq_into_parts(seq):
        color = '0'
        parts = []
        part = 0
        for am in seq:
            if am != color:
                #print(am, color, am != color)
                color = am
                parts.append(part)
                part = 1
            else:
                part += 1
        if part != 0:
            parts.append(part)
        return parts



