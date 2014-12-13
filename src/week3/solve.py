import sys

import numpy as np

from dictionary import construct_dictionary
from pivot import entering, leaving, pivot



def write_output(file_path, output):
    with open(file_path, 'w') as file:
        file.write('%s\n' % output)



def solve(dictionary):
    pivot_steps    = 0
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
        pivot_steps += 1



def dual(dictionary):
    dictionary[:-1, 1:] = -dictionary[:-1, 1:]
    dictionary[-2, 1] = 0
    for i in xrange(dictionary.shape[1] - 2):
        dictionary[-2, i + 2] = 1

    return dictionary[::-1].transpose()[::-1]



def restore(dictionary, obj_vals, obj_inds):
    final_dict  = dictionary[::-1].transpose()[::-1]
    final_dict[:-1, 1:] = -final_dict[:-1, 1:]

    new_inds = np.copy(final_dict[-1, 1:])

    for i in xrange(len(obj_inds)):
        if obj_inds[i] in new_inds and obj_inds[i] != new_inds[i]:
            for j in xrange(len(new_inds)):
                if obj_inds[i] == new_inds[j]:
                    obj_inds[i], obj_inds[j] = obj_inds[j], obj_inds[i]
                    obj_vals[i], obj_vals[j] = obj_vals[j], obj_vals[i]

    new_vals = np.copy(obj_vals)

    for i in xrange(len(new_inds)):
        if new_inds[i] not in obj_inds:
            new_vals[i] = 0

    column = final_dict[:-2, 0]
    for i in xrange(len(column)):
        if column[i] in obj_inds:
            for j in xrange(len(obj_inds)):
                if column[i] == obj_inds[j]:
                    value = obj_vals[j]
            new_vals += final_dict[i, 1:] * value

    final_dict[-2, 1:] = new_vals
    return final_dict



def initialize(dictionary, obj_vals, obj_inds):
    if dictionary[:-2, 1].min() < 0:
        dictionary = solve(dual(dictionary))
        if dictionary is not None:
            dictionary = restore(dictionary, obj_vals, obj_inds)

    return dictionary



def solve_dual(dictionary, obj_vals, obj_inds):
    dictionary = initialize(dictionary, obj_vals, obj_inds)
    if dictionary is None:
        return 'INFEASIBLE'
    else:
        dictionary = solve(dictionary)
        if dictionary is None:
            return 'UNBOUNDED'
        else:
            return '%0.6f' % dictionary[-2, 1]



def main(argv):
    np.seterr(divide = 'ignore', invalid = 'ignore')
    np.set_printoptions(linewidth = 200, precision = 2, suppress = True)

    dictionary = construct_dictionary(argv[0])
    obj_vals   = np.copy(dictionary[-2, 1:])
    obj_inds   = np.copy(dictionary[-1, 1:])

    write_output(argv[1], solve_dual(dictionary, obj_vals, obj_inds))



if __name__ == "__main__":
    main(sys.argv[1:])
