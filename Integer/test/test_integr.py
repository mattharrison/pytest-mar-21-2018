from integr import parse

import pytest


def test_basic():
    data = '1,3,5,9'
    res = parse(data)
    assert res == [1, 3, 5, 9]


def test_bad1():
    with pytest.raises(ValueError):
        parse('bad input')


@pytest.mark.xfail(raises=ValueError)
def test_bad2():
    parse('1-3,12-15')
