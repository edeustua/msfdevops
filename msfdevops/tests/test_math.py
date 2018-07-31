"""
Tests for msfdevops math modules
"""

from msfdevops import *
import pytest
import numpy as np
import itertools as it

@pytest.fixture()
def num_list_3():
    return [1, 2, 3, 4, 5]

@pytest.mark.parametrize("num_lst, expected_mean", [
    ( [1, 2, 3, 4, 5], 3 ),
    ( [0, 2, 4, 6], 3 ),
    ( [1, 2, 3, 4], 2.5),
    ( list(range(1, 100000)), 100000/2),
    ])
def test_many(num_lst, expected_mean):
    #assert math.mean(num_lst) == expected_mean
    assert np.isclose(math.mean(num_lst), expected_mean, 1e-6)

@pytest.mark.skipif(False, reason='comment')
def test_mean():
    num_lst = [1, 2, 3, 4, 5]
    observed = math.mean(num_lst)
    expected = 3.0
    assert observed == expected, 'Mean test failed'

@pytest.mark.my_easy_tests
def test_mean_list():
    num_tuple = (1, 2, 3, 4, 5)
    with pytest.raises(TypeError):
        math.mean(num_tuple)

    test_var = 8
    with pytest.raises(TypeError):
        math.mean(test_var)


    num_lst = [1, 2, 3, 'a', 'b', 'c']
    with pytest.raises(TypeError):
        math.mean(num_lst)


def test_empty_list():
    num_lst = []
    with pytest.raises(ZeroDivisionError):
        math.mean(num_lst)


def test_mean_fixture(num_list_3):
    assert math.mean(num_list_3) == 3, 'Mean test failed, fixture \
    version'

@pytest.mark.parametrize("x", it.permutations('ABC'))
def test_foo(x):
    print(x)
    pass

