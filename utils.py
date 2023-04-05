from os import system
from os import name as OS_NAME


def clear():
    """
        :ARGS:  
            None;

        :RETURNS:
            return None;

        :INFO:
            wipe the terminal screen;
    """

    if OS_NAME == "posix":
        # for *nix machines.
        system("clear")

    elif OS_NAME == "windows":
        system("cls")

    else:
        # for other system in the world
        # system("your-os-clear-command")
        pass

    return None


def print_sequence(sequence: list, series_type: str):
    """
        :ARGS:
            sequence:list => the discrete sequence;
            series_type:str => the series can be either 'dft' or 'idft'.

        :RETURNS:
            return None;

        :INFO:
            print the sequence that we get from either,
            'dft' or 'idft' function in nice way in terminal.
            and choose the right chars to represents the right series.

        """

    assert isinstance(
        sequence, list), f"the given sequence is not 'list' type its '{type(sequence)}'"

    assert isinstance(
        series_type, str), f"the given series-type is not 'str' type its '{type(sequence)}'"

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
