import simfold


def write_configurations(file, config_list):
    with open(file, 'w', encoding='utf-8') as w:
        for config in config_list:
            w.write(' '.join(config) + '\n')


if __name__ == '__main__':
    pf = simfold.SpiralFolding()
    pf.fold('sequences_public.txt')
    write_configurations('folding.txt', pf.get_folding_list())