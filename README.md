# NumX - Import Numbers

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/tomhea/numx)](https://github.com/tomhea/numx)
[![GitHub](https://img.shields.io/github/license/tomhea/numx)](LICENSE)
[![PyPI - Version](https://img.shields.io/pypi/v/numx)](https://pypi.org/project/numx/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/numx)](https://pypi.org/project/numx/)

Import numbers.

```python
>> from numx import p25
>> print(p25)
97
```

### How to Download
```
pip install numx
```

# Supported Number Types
- `pN`  - the Nth prime.
- `nN`  - the number N.
- `rN`  - random integer in range [0, N].
- `piN` - pi with N digits after the point precision.
- `eN`  - e with N digits after the point precision.

Moreover, for big numbers you can use: 
- `2e7` to denote `2 * 10**7`
- `2p7` to denote `2 ** 7`
- `_` as a dot, so: `6_25p_5` is `6.25 ** 0.5`

An import can fail only when importing a variable written in a bad format (e.g. numx.n7e will fail).  
When it fails, numx will raise the numx.__NumXError exception, which inherits from ValueError.
