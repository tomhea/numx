import pytest
import sympy

import numx
from numx import __NumXError as NumXError
from sympy import pi, E, N, Float


def test_p():
    assert numx.p25 == 97
    with pytest.raises(NumXError):
        numx.p0


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
        diffs.append(abs(N(number - num_digit_i)))

    assert sorted(diffs, reverse=True) == diffs


def test_pi():
    _assert_math_constant(pi, 'pi', 1000)


def test_e():
    _assert_math_constant(E, 'e', 1000)


def test_primes_upto_n():
    primes = list(sympy.sieve.primerange(1000))
    assert numx.PL0 == []
    assert numx.PL1 == []
    assert numx.PL2 == [2]
    assert numx.PL3 == [2, 3]
    assert numx.PL8 == [p for p in primes if p <= 8]
    assert numx.PL97 == [p for p in primes if p <= 97]
    assert numx.PL200 == [p for p in primes if p <= 200]


def test_num_of_primes_upto():
    primes = list(sympy.sieve.primerange(1000))
    assert numx.P0 == len([])
    assert numx.P1 == len([])
    assert numx.P2 == len([2])
    assert numx.P3 == len([2, 3])
    assert numx.P8 == len([p for p in primes if p <= 8])
    assert numx.P97 == len([p for p in primes if p <= 97])
    assert numx.P200 == len([p for p in primes if p <= 200])


def test_first_n_primes():
    primes = list(sympy.sieve.primerange(2000))
    assert numx.pl0 == primes[:0]
    assert numx.pl1 == primes[:1]
    assert numx.pl2 == primes[:2]
    assert numx.pl3 == primes[:3]
    assert numx.pl8 == primes[:8]
    assert numx.pl97 == primes[:97]
    assert numx.pl200 == primes[:200]


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


def test_inner_fails():
    with pytest.raises(AttributeError):
        numx.__all__
    assert 'Supported Number Types' in numx.__doc__
