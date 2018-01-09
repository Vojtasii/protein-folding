def fold (file):
    with open('folding.txt', 'w', encoding='utf-8') as w:
        with open(file, 'rt', encoding='utf-8') as f:
            for line in f:
                l = line.split()
                w.write(' '.join(l) + '\n')

if __name__ == '__main__':
    fold('sequences_public.txt')