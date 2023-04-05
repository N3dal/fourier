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
