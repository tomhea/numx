"""
With this package you can import numbers. For example:
from numx import p25   # == 97, the 25th prime
from numx import n300  # == 300

# Supported Number Types
- `pN` - the Nth prime.
- `nN` - the number N.ex

Moreover, for big numbers you can use:
- `2e7` to denote `2 * 10**7`
- `2p7` to denote `2 ** 7`
- `_` as a dot, so: `6_25p_5` is `6.25 ** 0.5`
"""

from numx._numx_main import _calculate_number


def __getattr__(request: str):
    return _calculate_number(request)
