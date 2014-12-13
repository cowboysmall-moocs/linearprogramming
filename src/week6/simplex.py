import sys

import numpy as np

from dictionary import construct_dictionary
from pivot import entering, leaving, pivot
from dual import dualize, restore



def write_output(file_path, output):
    with open(file_path, 'w') as file:
        file.write('%s\n' % output)



def solve(dictionary):
    entering_index = 0
    leaving_index  = 0

    while True:
        entering_index = entering(dictionary)
        if entering_index == -1:
            return dictionary

        leaving_index = leaving(dictionary, entering_index)
        if leaving_index == -1:
            return None

        dictionary = pivot(dictionary, entering_index, leaving_index)



def initialize(dictionary, obj_vals, obj_inds):
    if dictionary[:-2, 1].min() < 0:
        dictionary = solve(dualize(dictionary))
        if dictionary is not None:
            dictionary = restore(dictionary, obj_vals, obj_inds)

    return dictionary



def is_final(dictionary):
    return dictionary[-2, 2:].max() < 0



def solve_dual(dictionary):
    initialized = initialize(dictionary, np.copy(dictionary[-2, 1:]), np.copy(dictionary[-1, 1:]))

    if initialized is None:
        return 'INFEASIBLE'
    else:
        solved = solve(initialized)
        if solved is None:
            return 'UNBOUNDED'
        else:
            return solved



def main(argv):
    np.seterr(divide = 'ignore', invalid = 'ignore')
    np.set_printoptions(linewidth = 200, precision = 5, suppress = True)

    initial_dict = construct_dictionary(argv[0])
    final_dict   = solve_dual(initial_dict)

    print
    print initial_dict
    print
    print final_dict
    print

    # write_output(argv[1], '%0.6f' % final_dict[-2, 1])



if __name__ == "__main__":
    main(sys.argv[1:])
