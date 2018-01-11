from itertools import accumulate
import sys
import simfold
import folding_utils
from ComplexNumber import ComplexNumber

SEQ_DIR = 'sequences_public.txt'
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
    '''
    pf = simfold.SpiralFolding()
    pf.fold(SEQ_DIR)
    folding_list = pf.get_folding_list()
    #write_configurations(CONF_DIR, folding_list)
    '''
    pf2 = simfold.BedSheetFolding()
    pf2.fold(SEQ_DIR)
    folding_list2 = pf2.get_folding_list()
    write_configurations(CONF_DIR, folding_list2)
    '''
    total1 = 0
    total2 = 0
    for i, result in enumerate(zip(get_free_energy(SEQ_DIR, folding_list), get_free_energy(SEQ_DIR, folding_list2))):
        total1 += result[0]
        total2 += result[1]
    print('Spiral:', total1)
    print('Bed Sheet:', total2)
    '''
