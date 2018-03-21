from block import Amount


def test_amount_todict():
    a = Amount('matt', 5)
    res = a.todict()
    assert res == {'uuid': 'matt', 'amount': 5}


if __name__ == '__main__':
    import pytest
    pytest.main()
