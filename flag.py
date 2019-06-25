"""Japanese flag generator

This module contains an invalid function argument exception and
a function that forms a Japanese flag in ascii art.

"""

INVALID_ARGUMENT_MESSAGE = "N must be an integer even number."


class ArgumentError(Exception):
    """Exception that reporting about invalid function argument."""


def flag(n):
    """Return the Japanese flag in ASCII art."""
    if not isinstance(n, int) or n&1 != 0:
        raise ArgumentError(INVALID_ARGUMENT_MESSAGE)

    width = 3*n
    half_flag = ['#' * (width+2)]
    half_flag.extend([f"#{' '*width}#"] * (n//2))

    for i in range(n//2):
        circle_chord = f"*{'o' * 2*i}*"
        half_flag.append(f"#{circle_chord:^{width}}#")

    return '\n'.join(half_flag + half_flag[::-1])

if __name__ == "__main__":
    try:
        print(flag(int(input())))
    except ArgumentError as exc:
        print(str(exc))