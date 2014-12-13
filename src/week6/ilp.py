import sys
import math

import numpy as np

from dictionary import construct_dictionary
from pivot import entering, leaving, pivot
from dual import dualize, restore
from simplex import initialize, solve, is_final



def write_output(file_path, output):
    with open(file_path, 'w') as file:
        file.write('%s\n' % output)



def frac(x):
    return x - math.floor(x)



def add_cutting_planes(dictionary):
    dictionary = np.copy(dictionary)
    rows       = dictionary.shape[0]
    cols       = dictionary.shape[1]
    count      = rows + cols - 3

    new_rows = []
    for i in xrange(rows - 2):
        if 0.001 < frac(dictionary[i, 1]) < 0.999:
            row    = [0] * cols
            row[0] = count
            row[1] = -frac(dictionary[i, 1])
            for j in xrange(2, cols):
                row[j] = frac(-dictionary[i, j])
            new_rows.append(row)
            count += 1

    return np.insert(dictionary, -2, new_rows, axis = 0)



def is_ilp_final(dictionary, original_inds):
    column = dictionary[:-2, 0]
    for i in xrange(len(column)):
        if column[i] in original_inds:
            if 0.001 < frac(dictionary[i, 1]) < 0.999:
                return False
    return True



def solve_ilp(dictionary, indices):
    initialized = initialize(dictionary, np.copy(dictionary[-2, 1:]), np.copy(dictionary[-1, 1:]))

    if initialized is None:
        return 'INFEASIBLE'
    else:
        solved = solve(initialized)
        if solved is None:
            return 'UNBOUNDED'
        elif not is_ilp_final(solved, indices):
            return solve_ilp(add_cutting_planes(solved), indices)
        else:
            return solved



def main(argv):
    np.seterr(divide = 'ignore', invalid = 'ignore')
    np.set_printoptions(linewidth = 200, precision = 2, suppress = True)

    initial_dict = construct_dictionary(argv[0])
    final_dict   = solve_ilp(initial_dict, np.copy(initial_dict[-1, 2:]))

    # if not is_final(initial_dict):
    #     final_dict = solve_ilp(initial_dict, np.copy(initial_dict[-1, 2:]))
    # else:
    #     final_dict = 'INFEASIBLE'

    print
    print initial_dict
    print
    print final_dict
    print

    # write_output(argv[1], '%0.6f' % final_dict[-2, 1])



if __name__ == "__main__":
    main(sys.argv[1:])
