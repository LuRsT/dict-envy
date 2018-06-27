VERSION = (0, 1, 1)
__version__ = '.'.join(map(str, VERSION))


def merge(d1, d2):
    """Merges d2 into d1 without overwriting keys."""
    ret = d1.copy()
    for key in d2.keys():
        if key in ret:
            if isinstance(ret[key], dict):
                ret[key].update(merge(ret[key], d2[key]))
        else:
            ret[key] = d2[key]
    return ret


def dict_from_key_path(segments, value):
    """Creates a nested dict out of array of keys."""
    ret = {}
    for segment in reversed(segments):
        if ret:
            ret = {segment: ret}
        else:
            ret[segment] = value
    return ret


def dictate(store, depth):
    """Transforms environment variables into a dictionary.

    Key in conjugation with depth is what controls the depth of the nested
    dicts.

    Examples:
        store={'A_B_C': 1}, depth=0 => {'a_b_c': 1}}
        store={'A_B_C': 1}, depth=1 => {'a': {'b_c': 1}}
        store={'A_B_C': 1}, depth=2 => {'a': {'b': {'c': 1}}}
    """
    ret = {}
    for key, value in store.items():
        # fixme: provide a mapping to dictate() instead of using .replace() on key
        parts = key.lower().replace('__', '').split('_', depth)
        dict_value = dict_from_key_path(parts, value)
        ret = merge(ret, dict_value)
    return ret
