import sys

import numpy as np

from dictionary import construct_dictionary


def write_output(file_path, dictionary, entering, leaving):
    with open(file_path, 'w') as file:
        if leaving == -1:
            file.write('UNBOUNDED\n')
        else:
            file.write('%0.0f\n' % dictionary[leaving, 0])
            file.write('%0.0f\n' % dictionary[-1, entering])
            file.write('%0.2f\n' % dictionary[-2, 1])


def entering(dictionary):
    ordering = []

    for i in xrange(2, dictionary.shape[1]):
        if dictionary[-2, i] > 0:
            ordering.append((dictionary[-1, i], i))

    ordering.sort()
    if len(ordering) == 0:
        return -1
    else:
        return ordering[0][1]


def leaving(dictionary, entering_index):
    ordering = []
    bounds   = dictionary[:-2, 1] / dictionary[:-2, entering_index]

    for i in xrange(dictionary.shape[0] - 2):
        if dictionary[i, entering_index] < 0:
            ordering.append((bounds[i], dictionary[i, 0], i))

    ordering.sort(reverse = True, key = lambda x: (x[0], -x[1]))
    if len(ordering) == 0:
        return -1
    else:
        return ordering[0][2]


def pivot(dictionary, entering, leaving):
    new_dictionary = np.copy(dictionary)
    new_dictionary[leaving, entering] = -1

    new_dictionary[leaving, 1:] /= -dictionary[leaving, entering]

    rows = new_dictionary.shape[0]
    cols = new_dictionary.shape[1]

    for i in xrange(0, rows - 1):
        if i != leaving:
            for j in xrange(1, cols):
                if j != entering:
                    new_dictionary[i, j] += dictionary[i, entering] * new_dictionary[leaving, j]
                else:
                    new_dictionary[i, j]  = dictionary[i, entering] * new_dictionary[leaving, j]

    new_dictionary[leaving, 0], new_dictionary[-1, entering] = new_dictionary[-1, entering], new_dictionary[leaving, 0]
    return new_dictionary


def main(argv):
    np.seterr(divide = 'ignore', invalid = 'ignore')

    dictionary     = construct_dictionary(argv[0])
    entering_index = entering(dictionary)
    leaving_index  = leaving(dictionary, entering_index)
    new_dictionary = pivot(dictionary, entering_index, leaving_index)

    print dictionary
    print
    print new_dictionary

    write_output(argv[1], new_dictionary, entering_index, leaving_index)


if __name__ == "__main__":
    main(sys.argv[1:])
