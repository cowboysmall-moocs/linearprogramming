import sys

import numpy as np

from dictionary import construct_dictionary
from pivot import entering, leaving, pivot


def write_output(file_path, dictionary, steps, solved):
    with open(file_path, 'w') as file:
        if not solved:
            file.write('UNBOUNDED\n')
        else:
            file.write('%0.6f\n' % dictionary[-2, 1])
            file.write('%0.0f\n' % steps)


def solve(dictionary):
    pivot_steps    = 0
    entering_index = 0
    leaving_index  = 0
    current        = dictionary

    while True:
        entering_index = entering(current)
        if entering_index == -1:
            return current, pivot_steps, True

        leaving_index = leaving(current, entering_index)
        if leaving_index == -1:
            return None, 0, False

        current = pivot(current, entering_index, leaving_index)
        pivot_steps += 1


def main(argv):
    np.seterr(divide = 'ignore', invalid = 'ignore')

    initial_dictionary        = construct_dictionary(argv[0])
    dictionary, steps, solved = solve(initial_dictionary)

    print dictionary

    # write_output(argv[1], dictionary, steps, solved)


if __name__ == "__main__":
    main(sys.argv[1:])
