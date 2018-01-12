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
        conf_dict = {}
        max_row = 20 if seq_len > 20 else seq_len
        for row in range(1, max_row):
            conf_dict[row] = self.free_energy(seq, self.fold_sheet(seq_parts, row, seq_len))
        best_row = min(conf_dict.keys(), key=(lambda k: conf_dict[k]))
        return self.fold_sheet(seq_parts, best_row, seq_len)

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
        bend = ComplexNumber(0, 1)
        color, first_row, loop, step, back = True, True, 0, 0, 0
        part = next(iter_parts)
        next_part = part
        tmp_len = len(tmp)
        for i in range(tmp_len):
            step += 1
            if i + 1 == next_part:
                color = not color
                part = next(iter_parts)
                next_part += part
            if color and loop > 0:
                if loop == 2:
                    tmp[i] *= ComplexNumber(0, 1)
                    step += 1
                else:
                    tmp[i] = ComplexNumber(1, 0)
                step -= back
                back = 0
                loop = -1

            elif not color and first_row and part > 1 and loop != -1:
                loop = 1 if part % 2 else 2
                step -= 1
                back -= 1
                loop_step = i - next_part + part + 1
                if loop_step < part // 2:
                    tmp[i] *= ComplexNumber(0, -1)
                elif loop_step > part // 2:
                    tmp[i] *= ComplexNumber(0, 1)
            elif step == row:
                loop = 0
                first_row = False
                overhang = next_part - i - 1
                if not color and overhang >= 2 - back:
                    step -= 1
                    back -= 1
                else:
                    tmp[i] *= bend
                    tmp = [c * ComplexNumber(-1, 0) if k > i else c for k, c in enumerate(tmp)]
                    bend *= ComplexNumber(-1, 0)
                    step = back
                    back = 0
            elif loop == -1:
                loop = 0
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
