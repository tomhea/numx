import random
from typing import List

from sympy import N, Float, prime, sieve, primepi, pi, E

from numx._exceptions import NumXError, NuxXNotImplementedError


def return_same(number: int) -> int:
    return number


def calc_nth_prime(number: int) -> int:
    if number <= 0:
        raise NumXError("The prime number index must be positive")
    return prime(number)


def random_number(number: int) -> int:
    return random.randint(0, number)


def py_nth_point(number: int) -> Float:
    return N(pi, number + 1)


def e_nth_point(number: int) -> Float:
    return N(E, number + 1)


def first_n_primes(number: int) -> List[int]:
    if number == 0:
        return []
    return primes_upto_n(calc_nth_prime(number))


def num_of_primes_upto(number: int) -> int:
    return int(primepi(number))


def primes_upto_n(number: int) -> List[int]:
    return list(sieve.primerange(number + 1))


def euler_totient(number: int) -> int:
    raise NuxXNotImplementedError("The function 'euler_totient()' is not implemented yet.")


def factorial(number: int) -> int:
    raise NuxXNotImplementedError("The function 'factorial()' is not implemented yet.")


def fibonacci(number: int) -> int:
    raise NuxXNotImplementedError("The function 'fibonacci()' is not implemented yet.")
