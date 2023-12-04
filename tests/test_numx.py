import pytest
import numx
from numx._exceptions import NumXError


def test_p():
    assert numx.p25 == 97
    with pytest.raises(NumXError):
        numx.p0


def test_n():
    assert numx.n25 == 25
    assert numx.n0 == 0


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
    assert numx.__doc__
