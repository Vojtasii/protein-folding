from itertools import accumulate
import simfold
import folding_utils


SEQ_DIR = 'sequences_public.txt'
CONF_DIR = 'folding.txt'


def write_configurations(file, config_list):
    with open(file, 'w', encoding='utf-8') as w:
        for config in config_list:
            w.write(' '.join([str(c) for c in config]) + '\n')


def write_free_energy(file, config_list):
    for s, c in zip(folding_utils.read_from_file(SEQ_DIR), config_list):
        p = [0]
        p.extend(accumulate(c))
        folding_utils.compute_free_energy(s, p)


if __name__ == '__main__':
    pf = simfold.SpiralFolding()
    pf.fold('sequences_public.txt')
    folding_list = pf.get_folding_list()
    write_configurations('folding.txt', folding_list)
    write_free_energy(SEQ_DIR, folding_list)