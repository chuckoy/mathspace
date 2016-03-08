import argparse
import sys
import timeit

from decimal import *

n = 1

def main(argv):
    parser = argparse.ArgumentParser(
        description='Problem B solution')
    parser.add_argument('-n', '--n', metavar='n', nargs=1,
                        help='The sides of the dice (default=1)')

    args = parser.parse_args()
    if args.n:
        n = int(args.n[0])
    for i in range(1, n + 1):
        t = timeit.Timer('roll(n)', 'from __main__ import roll; n=%d' % i)
        print("i={0} time={1}".format(i, str(t.timeit(1))))


def roll(n):
    """
    Calculate probability for an n-sided die labelled with integers from
    1 to n, to roll all the numbers {1, ..., n}, in any order if the die
    is thrown n times

    Keyword arguments:
    n -- sides of the dice
    """
    remaining_num = list(reversed([x for x in range(1, n)]))
    probability = Decimal(1)
    n = Decimal(n)
    for num in remaining_num:
        probability *= Decimal(num) / n
    return probability


if __name__ == "__main__":
    main(sys.argv[1:])
