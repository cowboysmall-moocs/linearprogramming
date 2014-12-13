import sys

import numpy as np



def construct_dictionary(file_path):
    with open(file_path) as file:
        dimensions = file.readline().split()
        m = int(dimensions[0])
        n = int(dimensions[1])

        dictionary = np.zeros((m + 2, n + 2))

        basic = file.readline().split()
        for i in xrange(m):
            dictionary[i, 0] = int(basic[i])

        non_basic = file.readline().split()
        for i in xrange(n):
            dictionary[m + 1, i + 2] = int(non_basic[i])

        b = file.readline().split()
        for i in xrange(m):
            dictionary[i, 1] = float(b[i])

        for i in xrange(m):
            row_coefficients = file.readline().split()
            for j in xrange(n):
                dictionary[i, j + 2] = float(row_coefficients[j])

        obj_coefficients = file.readline().split()
        for i in xrange(n + 1):
            dictionary[m, i + 1] = float(obj_coefficients[i])

    return dictionary


def main(argv):
    np.seterr(divide = 'ignore', invalid = 'ignore')
    np.set_printoptions(linewidth = 200, precision = 2, suppress = True)

    dictionary = construct_dictionary(argv[0])

    print
    print dictionary
    print 


if __name__ == "__main__":
    main(sys.argv[1:])
