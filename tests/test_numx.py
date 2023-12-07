import pytest
import sympy

import numx
from numx import __NumXError as NumXError
from sympy import Float


# noinspection PyStatementEffect
def test_p():
    assert numx.p25 == 97
    with pytest.raises(NumXError):
        numx.p0


def test_pl():
    primes = list(sympy.sieve.primerange(2000))
    assert numx.pl0 == primes[:0]
    assert numx.pl1 == primes[:1]
    assert numx.pl2 == primes[:2]
    assert numx.pl3 == primes[:3]
    assert numx.pl8 == primes[:8]
    assert numx.pl97 == primes[:97]
    assert numx.pl200 == primes[:200]


# noinspection PyPep8Naming
def test_P():
    primes = list(sympy.sieve.primerange(1000))
    assert numx.P0 == len([])
    assert numx.P1 == len([])
    assert numx.P2 == len([2])
    assert numx.P3 == len([2, 3])
    assert numx.P8 == len([p for p in primes if p <= 8])
    assert numx.P97 == len([p for p in primes if p <= 97])
    assert numx.P200 == len([p for p in primes if p <= 200])


# noinspection PyPep8Naming
def test_PL():
    primes = list(sympy.sieve.primerange(1000))
    assert numx.PL0 == []
    assert numx.PL1 == []
    assert numx.PL2 == [2]
    assert numx.PL3 == [2, 3]
    assert numx.PL8 == [p for p in primes if p <= 8]
    assert numx.PL97 == [p for p in primes if p <= 97]
    assert numx.PL200 == [p for p in primes if p <= 200]


def test_n():
    assert numx.n25 == 25
    assert numx.n0 == 0


def test_r():
    r1e6_max = 1_000_000
    length = 100_000

    sum_r = 0
    for _ in range(length):
        value = numx.r1e6
        assert 0 <= value <= r1e6_max
        sum_r += value

    assert 0.4 * r1e6_max < sum_r // length < 0.6 * r1e6_max


def _assert_math_constant(number: Float, number_type_string: str, test_length: int):
    diffs = []
    for i in range(test_length):
        num_digit_i = numx.__getattr__(f'{number_type_string}{i}')
        assert len(str(num_digit_i)) == i + 2
        diffs.append(abs(sympy.N(number - num_digit_i)))

    assert sorted(diffs, reverse=True) == diffs


def test_pi():
    _assert_math_constant(sympy.pi, 'pi', 1000)


def test_e():
    _assert_math_constant(sympy.E, 'e', 1000)


# noinspection PyStatementEffect
def test_t():
    with pytest.raises(NumXError):
        numx.t0

    for p in range(20):
        num = 10 * (10**p)
        tot = 4 * (10**p)
        assert numx.__getattr__(f't{num}') == tot

    for p in range(20):
        num = 3 * (3**p)
        tot = 2 * (3**p)
        assert numx.__getattr__(f't{num}') == tot

    for n in range(1, 10000):
        assert numx.__getattr__(f't{n}') == sympy.totient(n)


def test_fa():
    assert numx.fa0 == 1
    factorial = 1
    for n in range(1, 1000):
        factorial *= n
        assert numx.__getattr__(f'fa{n}') == factorial


def test_fi():
    fib, next_fib = 0, 1
    for i in range(1000):
        assert numx.__getattr__(f'fi{i}') == fib
        fib, next_fib = next_fib, fib + next_fib


def test_n_all_number_variations():
    assert numx.n25 == 25
    assert numx.n0 == 0

    assert numx.n2e18 == 2e18
    assert numx.n2_5e7 == round(2.5e7)
    assert numx.n2_5e7_5 == round(2.5 * 10**7.5)
    assert numx.n2e7_5 == round(2 * 10**7.5)

    assert numx.n3p7 == 3**7
    assert numx.n3_5p7 == round(3.5**7)
    assert numx.n3p7_5 == round(3**7.5)
    assert numx.n3_5p7_5 == round(3.5**7.5)

    assert numx.n_32e7 == round(.32 * 10**7)
    assert numx.n7000p_5 == round(7000 ** .5)


# noinspection DuplicatedCode,PyStatementEffect
def test_number_variations_fails():
    with pytest.raises(NumXError):
        numx.n
    with pytest.raises(NumXError):
        numx.blabla

    with pytest.raises(NumXError):
        numx.n_
    with pytest.raises(NumXError):
        numx.n2_
    with pytest.raises(NumXError):
        numx.n1_2
    with pytest.raises(NumXError):
        numx.n_2

    with pytest.raises(NumXError):
        numx.n1p
    with pytest.raises(NumXError):
        numx.n1e
    with pytest.raises(NumXError):
        numx.np1
    with pytest.raises(NumXError):
        numx.ne1

    with pytest.raises(NumXError):
        numx.n1e1e
    with pytest.raises(NumXError):
        numx.n1p1p
    with pytest.raises(NumXError):
        numx.n1e1p
    with pytest.raises(NumXError):
        numx.n1p1e

    with pytest.raises(NumXError):
        numx.n1p_
    with pytest.raises(NumXError):
        numx.n1e_
    with pytest.raises(NumXError):
        numx.n1p1_
    with pytest.raises(NumXError):
        numx.n1e1_


def test_help_works():
    help(numx)


# noinspection PyStatementEffect
def test_inner_fails_yet_wanted_succeed():
    with pytest.raises(AttributeError):
        numx.__all__
    assert numx.__NumXError
    assert 'Supported Number Types' in numx.__doc__
