import math
from itertools import accumulate
import operator
import folding_utils
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
        configuration = super().find_folding(seq)
        conf_dict = {}
        limit = int(math.ceil(math.sqrt(seq_len - seq_parts[0]) / 2))
        for row in range(limit, seq_len):
            conf_dict[row] = self.free_energy(seq, self.fold_sheet(seq_parts, row, seq_len))
        return self.fold_sheet(seq_parts, min(conf_dict, key=conf_dict.get), seq_len)

    @staticmethod
    def free_energy(seq, conf):
        p = [ComplexNumber(0, 0)]
        p.extend(accumulate(conf))
        return folding_utils.compute_free_energy(seq, p)

    @staticmethod
    def fold_sheet(parts, row, length):
        iter_parts = iter(parts)
        part = next(iter_parts)
        configuration = [ComplexNumber(1, 0)] * part  # Skip leading zeroes
        tmp = [ComplexNumber(1, 0)] * (length - 1 - part)
        conf = ComplexNumber(0, 1)
        color = True
        step = 0
        back = 0
        part = next(iter_parts)
        next_part = part
        tmp_len = len(tmp)
        for i in range(tmp_len):
            step += 1
            if i + 1 == next_part:
                color = not color
                part = next(iter_parts)
                next_part += part
            if step == row:
                overhang = next_part - i - 1
                if not color and overhang >= 2 - back:
                    step -= 1
                    back -= 1
                else:
                    tmp[i] *= conf
                    tmp = [c * ComplexNumber(-1, 0) if k > i else c for k, c in enumerate(tmp)]
                    conf *= ComplexNumber(-1, 0)
                    step = back
                    back = 0
        configuration.extend(tmp)
        return configuration

    @staticmethod
    def separate_seq_into_parts(seq):
        color = '0'
        parts = []
        part = 0
        for am in seq:
            if am != color:
                color = am
                parts.append(part)
                part = 1
            else:
                part += 1
        if part != 0:
            parts.append(part)
        return parts
