# dict-envy

dict-like grouping of environment variables :sparkles:

---

Imagine you have this:

```
COUNTRIES_GB_NAME="United Kingdom"
COUNTRIES_GB_TLD=.uk
COUNTRIES_HK_NAME=China
COUNTRIES_HK_TLD=.cn
```

and with a simple call you can have all of this:

```python
>>> import os
>>> import dictenvy
>>> import pprint
>>> env = dictenvy.dictate(os.environ, depth=2)
>>> pprint.pprint(env)
{'countries': {'gb': {'name': 'United Kingdom', 'tld': '.uk'},
               'hk': {'name': 'China', 'tld': '.cn'}}}
```

`depth` is how you regulate the depth of the returned dictionary.

## Installation

Use pip:

```shell
$ pip install dict-envy
```
