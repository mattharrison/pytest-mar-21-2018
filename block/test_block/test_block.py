from block import Amount, Block, Node, Transaction


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


def test_block():
    b = Block([], '')
    assert b.todict() == {'body':
        {'txns': []},
        'header': {'body_hash': '5c12d30d9ba5ddf3b2ba5ae8bf652b902fb005f91e2e0877269b5a9cec975052', 'nonce': None, 'prev_hash': ''}}


def test_txn():
    node = Node('matt')
    gb, hash = node.process_txns([])
    assert hash.startswith('0')
    

if __name__ == '__main__':
    import pytest
    pytest.main()
