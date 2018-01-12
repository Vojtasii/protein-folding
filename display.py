from display_utils import *
from folding_utils import compute_free_energy
from ComplexNumber import ComplexNumber
import time

SEQ_DIR = 'sequences.txt'
CONF_DIR = 'folding.txt'

COMPLEX = {'1': (1, 0), '-1': (-1, 0), '1j': (0, 1), '-1j': (0, -1)}

def to_complex(conf):
    """ Converts a configuration list into list of complex numbers for later use """

    return [ComplexNumber(COMPLEX[c][0], COMPLEX[c][1]) for c in conf]

def display(configuration, sequences):
    """ The Method of all methods that put it all together and display
    how the brand-new calculated structure of amino acid might look like
    in a fancy way of course :)
    """
    w = create_window()
    ninja_turtles = summon_ninja_turtles()
    counter = 0

    # opes the files
    with open(configuration, 'rt', encoding='utf-8') as fc, \
            open(sequences, 'rt', encoding='utf-8') as fs:
        # ... reads them line by line
        for conf, seq in zip(fc, fs):
            counter += 1
            conf = conf.split()
            seq = seq.split()
            energy = compute_free_energy(seq, to_complex(conf))

            #w.tracer(0,0)

            # ... makes ninja turtles do their jobs
            update_text(counter, len(seq), round(energy, 3))
            draw_conf(conf, seq)
            # ... a little rest here
            time.sleep(.4)
            # ...
            draw_arrow()

            #w.update()
            # ... gives the viewer some extra time to appreciate the beauty of folded protein
            time.sleep(.6)

            #time.sleep(2)

            # ... orders turtles to clean up the mess and start drawing again
            for i in ninja_turtles:
                i.clear()

    # THE END :)
    w.exitonclick()

if __name__ == '__main__':
    display(CONF_DIR, SEQ_DIR)
