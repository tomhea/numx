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
- `pN` - the Nth prime.
- `nN` - the number N.

Moreover, for big numbers you can use: 
- `2e7` to denote `2 * 10**7`
- `2p7` to denote `2 ** 7`
- `_` as a dot, so: `6_25p_5` is `6.25 ** 0.5`