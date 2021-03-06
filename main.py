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


from os import system
from os import name as OS_NAME
from math import (pi, sqrt, sin, cos)
from cmath import exp  # the normal exp from math module will not work.


# todo: make the script work from the command line directly, by passing args.


def clear():
    """wipe terminal screen."""

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for other system in the world
        # system("your-os-clear-command")
        pass


clear()


def dft(sequence: list):
    """calculate discrete-fourier-transform for given sequence."""

    N = len(sequence)

    # define x(k):
    def x(k: int): return sum(sequence_value*exp((-1j*2*pi*k*i)/N)
                              for i, sequence_value in enumerate(sequence))

    return [x(k) for k in range(N)]


def idft(sequence: list):
    """calculate inverse-discrete-fourier-transform for given sequence."""

    N = len(sequence)

    # define x(n):
    def x(k: int): return (1/N) * sum(sequence_value*exp((1j*2*pi*k*i)/N)
                                      for i, sequence_value in enumerate(sequence))

    return [x(k) for k in range(N)]


def print_sequence(sequence: list, series_type: str):
    """simple function to print the sequence that we get from either,
    'dft' or 'idft' function in nice way in terminal.
    and choose the right chars to represents the right series."""

    SERIES_TYPES = (
        "dft", "idft",  # dft types.
    )

    # guard-conditions.
    if series_type not in SERIES_TYPES:
        print("this series type not exist!!.")
        return None

    if series_type == "dft":
        series_symbol = "x̄"

    elif series_type == "idft":
        series_symbol = "x"

    print(f"{series_symbol}(k)\t Real\t Imag")
    for index, item in enumerate(sequence):
        print(f"{series_symbol}({index})\t  ", end='')
        print(
            f"{str(round(item.real)).center(2)}\t {(str(round(item.imag))+'j').center(3)}")

    return None


def main():
    l = dft([*range(3), 2j])
    il = idft(l)

    print_sequence(l, "dft")

    print("#" * 25)

    print_sequence(il, "idft")


if __name__ == "__main__":
    main()
