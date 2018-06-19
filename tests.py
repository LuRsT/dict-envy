import dictenvy


def test_transforms_into_dict():
    store = {'A': 1}
    assert dictenvy.dictate(store, depth=1) == {'a': 1}


def test_transforms_into_dict_one_level():
    store = {'A_B': 1}
    assert dictenvy.dictate(store, depth=1) == {'a': {'b': 1}}


def test_transforms_into_dict_one_level_with_one_underscore():
    store = {'A_B_HELLO': 1}
    assert dictenvy.dictate(store, depth=1) == {'a': {'b_hello': 1}}


def test_transforms_into_dict_two_levels():
    store = {'A_B_C': 1}
    assert dictenvy.dictate(store, depth=2) == {'a': {'b': {'c': 1}}}


def test_transforms_into_dict_two_levels_two_items_with_one_underscore():
    store = {'A_B_C_HELLO': 1, 'A_B_C_WORLD': 2}
    assert dictenvy.dictate(store, depth=2) == {'a': {'b': {'c_hello': 1, 'c_world': 2}}}


def test_transforms_into_dict_three_levels_with_two_items():
    store = {'A_B_C_HELLO': 1, 'A_B_C_WORLD': 2}
    assert dictenvy.dictate(store, depth=3) == {'a': {'b': {'c': {'hello': 1, 'world': 2}}}}
