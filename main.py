#!/usr/bin/python3
# -----------------------------------------------------------------
# simple script contain common fourier functions for ex:
# DFT, FFT, FOURIER-SERIES, ....., etc.
#
#
#
# Author:N84.
#
# Create Date:Wed Jun 22 23:21:41 2022.
# ///
# ///
# ///
# -----------------------------------------------------------------


from math import (pi, sqrt, sin, cos)
from cmath import exp  # the normal exp from math module will not work.
from utils import *

# todo: make the script work from the command line directly, by passing args.


clear()


def dft(sequence: list):
    """
        :ARGS:
            sequence:list => the discrete sequence;

        :RETURNS:
            return list;

        :INFO:
            calculate discrete-fourier-transform for given sequence.
    """

    assert isinstance(
        sequence, list), f"the given sequence is not 'list' type its '{type(sequence)}'"

    N = len(sequence)

    # define x(k):
    def x(k: int): return sum(sequence_value*exp((-1j*2*pi*k*i)/N)
                              for i, sequence_value in enumerate(sequence))

    return [x(k) for k in range(N)]


def idft(sequence: list):
    """
        :ARGS:
            sequence:list => the dft discrete sequence;

        :RETURNS:
            return list;

        :INFO:
            calculate inverse-discrete-fourier-transform for given sequence.
        """

    assert isinstance(
        sequence, list), f"the given sequence is not 'list' type its '{type(sequence)}'"

    N = len(sequence)

    # define x(n):
    def x(k: int): return (1/N) * sum(sequence_value*exp((1j*2*pi*k*i)/N)
                                      for i, sequence_value in enumerate(sequence))

    return [x(k) for k in range(N)]


def main():

    s = [*range(1, 101)]

    dft_s = dft(s)

    print_sequence(dft_s, "dft")


if __name__ == "__main__":
    main()
