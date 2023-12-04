import sympy

from numx._exceptions import NumXError


def return_same(number: int) -> int:
    return number


def calc_nth_prime(number: int) -> int:
    if number <= 0:
        raise NumXError("The prime number index must be positive")
    return sympy.prime(number)
