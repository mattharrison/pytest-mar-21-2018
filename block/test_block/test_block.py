from block import Amount, Transaction


def test_amount_todict():
    a = Amount('matt', 5)
    res = a.todict()
    assert res == {'uuid': 'matt', 'amount': 5}


def test_transaction():
    t = Transaction([Amount('matt', 5)],
                    [Amount('matt', 1),
                     Amount('fred', 4)])
    assert t.todict() == {'inputs': [{'amount': 5, 'uuid': 'matt'}],
          'outputs': [{'amount': 1, 'uuid': 'matt'}, {'amount': 4, 'uuid': 'fred'}]}


if __name__ == '__main__':
    import pytest
    pytest.main()
