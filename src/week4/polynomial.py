import sys
import pylab

import numpy as np

from cvxopt import matrix
from cvxopt.lapack import gels


def read_data(file_path):
    t = []
    y = []

    with open(file_path) as file:
        for line in file:
            values = line.split()
            t.append(float(values[0]))
            y.append(float(values[1]))

    return matrix(t), matrix(y)


def plot_poly(t, y, c, degree):
    ts = np.linspace(min(t), max(t), len(t))
    ys = sum( [c[k] * (ts ** k) for k in xrange(degree + 1)] )

    pylab.figure(1, facecolor = 'w')
    pylab.plot(t, y, '.r', label = 'data')
    pylab.plot(ts, ys, '-b', label = 'polynomial')

    pylab.xlabel('x')
    pylab.ylabel('P(x)')
    pylab.axis([min(t), max(t), min(y), max(y)])
    pylab.title('Polynomial: Degree %s' % degree)
    pylab.legend(loc = 'lower right')
    pylab.show()


def main(argv):
    t, y   = read_data(argv[0])
    degree = int(argv[1])

    A = +matrix( [[t ** k] for k in xrange(degree + 1)] )
    c = +y

    gels(A, c)

    print c[:degree + 1]
    plot_poly(t, y, c, degree)


if __name__ == "__main__":
    main(sys.argv[1:])
