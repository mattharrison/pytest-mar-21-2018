from integr import parse

import pytest


def test_basic():
    data = '1,3,5,9'
    res = parse(data)
    print(f'Res {res}')
    assert res == [0, 3, 5, 9]


def test_bad1():
    with pytest.raises(ValueError):
        parse('bad input')


@pytest.mark.xfail(raises=ValueError)
def test_bad2():
    parse('1-3,12-15')


if __name__ == '__main__':
    pytest.main()
