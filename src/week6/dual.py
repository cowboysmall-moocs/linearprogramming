import sys

import numpy as np

from dictionary import construct_dictionary



def dualize(dictionary):
    dictionary          = np.copy(dictionary)
    dictionary[:-1, 1:] = -dictionary[:-1, 1:]
    dictionary[-2, 1]   = 0

    for i in xrange(dictionary.shape[1] - 2):
        dictionary[-2, i + 2] = 1

    dictionary         = dictionary[::-1].transpose()[::-1]
    dictionary[:, 2:]  = dictionary[:, 2:][:, ::-1]
    dictionary[:-2, :] = dictionary[:-2, :][::-1]

    return dictionary


def restore_order(obj_vals, obj_inds, new_inds):
    for i in xrange(len(obj_inds)):
        if obj_inds[i] in new_inds and obj_inds[i] != new_inds[i]:
            for j in xrange(len(new_inds)):
                if obj_inds[i] == new_inds[j]:
                    obj_inds[i], obj_inds[j] = obj_inds[j], obj_inds[i]
                    obj_vals[i], obj_vals[j] = obj_vals[j], obj_vals[i]


def restore(dictionary, obj_vals, obj_inds):
    dictionary          = np.copy(dictionary)
    dictionary          = dictionary[::-1].transpose()[::-1]
    dictionary[:-2, :]  = dictionary[:-2, :][::-1]
    dictionary[:, 2:]   = dictionary[:, 2:][:, ::-1]

    dictionary[:-1, 1:] = -dictionary[:-1, 1:]

    new_inds = np.copy(dictionary[-1, 1:])
    restore_order(obj_vals, obj_inds, new_inds)
    new_vals = np.copy(obj_vals)

    for i in xrange(len(new_inds)):
        if new_inds[i] not in obj_inds:
            new_vals[i] = 0

    column = dictionary[:-2, 0]
    for i in xrange(len(column)):
        if column[i] in obj_inds:
            for j in xrange(len(obj_inds)):
                if column[i] == obj_inds[j]:
                    value = obj_vals[j]
            new_vals += dictionary[i, 1:] * value

    dictionary[-2, 1:] = new_vals
    return dictionary



def main(argv):
    np.seterr(divide = 'ignore', invalid = 'ignore')
    np.set_printoptions(linewidth = 200, precision = 5, suppress = True)

    initial_dict  = construct_dictionary(argv[0])
    dual_dict     = dual(initial_dict)
    restored_dict = restore(dual_dict, np.copy(initial_dict[-2, 1:]), np.copy(initial_dict[-1, 1:]))

    print
    print initial_dict
    print
    print dual_dict
    print 
    print restored_dict
    print



if __name__ == "__main__":
    main(sys.argv[1:])
