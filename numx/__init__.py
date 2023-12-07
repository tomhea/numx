"""
With this package you can import numbers. For example:
from numx import p25   # == 97, the 25th prime
from numx import n300  # == 300

# Supported Number Types
- `pN`  - the Nth prime.
- `nN`  - the number N.ex
- `rN`  - random integer in range [0, N].
- `piN` - pi with N digits after the point precision.
- `eN`  - e with N digits after the point precision.

Moreover, for big numbers you can use:
- `2e7` to denote `2 * 10**7`
- `2p7` to denote `2 ** 7`
- `_` as a dot, so: `6_25p_5` is `6.25 ** 0.5`

An import can fail only when importing a variable written in a bad format (e.g. numx.n7e will fail).
When it fails, numx will raise the numx.__NumXError exception, which inherits from ValueError.
"""

from numx._numx_main import _calculate_number
from numx._exceptions import NumXError as __NumXError


def __getattr__(request: str):
    return _calculate_number(request)
