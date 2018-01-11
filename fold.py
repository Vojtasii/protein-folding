from itertools import accumulate
import simfold
import folding_utils
from ComplexNumber import ComplexNumber

SEQ_DIR = 'sequences.txt'
CONF_DIR = 'folding.txt'


def write_configurations(file, config_list):
    with open(file, 'w', encoding='utf-8') as w:
        for config in config_list:
            w.write(' '.join([str(c) for c in config]) + '\n')


def get_free_energy(file, config_list):
    for s, c in zip(folding_utils.read_from_file(SEQ_DIR), config_list):
        p = [ComplexNumber(0, 0)]
        p.extend(accumulate(c))
        yield folding_utils.compute_free_energy(s, p)


if __name__ == '__main__':
    pf = simfold.BedSheetFolding()
    pf.fold(SEQ_DIR)
    folding_list = pf.get_folding_list()
    write_configurations(CONF_DIR, folding_list)

