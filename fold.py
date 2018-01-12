from itertools import accumulate
import simfold
import folding_utils
from ComplexNumber import ComplexNumber

SEQ_FILE = 'sequence.txt'
#SEQ_FILE = 'sequences_public.txt'
CONF_FILE = 'folding.txt'


def write_configurations(file, config_list):
    with open(file, 'w', encoding='utf-8') as w:
        for config in config_list:
            w.write(' '.join([str(c) for c in config]) + '\n')


def get_free_energy(file, config_list):
    for s, c in zip(folding_utils.read_from_file(SEQ_FILE), config_list):
        p = [ComplexNumber(0, 0)]
        p.extend(accumulate(c))
        yield folding_utils.compute_free_energy(s, p)


if __name__ == '__main__':
    pf = simfold.BedSheetFolding()
    pf.fold(SEQ_FILE)
    folding_list = pf.get_folding_list()
    #write_configurations(CONF_FILE, folding_list)
    old = simfold.BedSheetFoldingOld()
    old.fold(SEQ_FILE)
    folding_list_old = old.get_folding_list()
    write_configurations(CONF_FILE, folding_list_old)
    total = 0
    total_old = 0
    for i, fe in enumerate(zip(get_free_energy(CONF_FILE, folding_list), get_free_energy(CONF_FILE, folding_list_old))):
        print(i + 1, fe[0], fe[1], fe[0] - fe[1])
        total += fe[0]
        total_old += fe[1]
    print(total, total_old)


