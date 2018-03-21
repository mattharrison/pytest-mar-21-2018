from integr import parse

def test_basic():
    data = '1,3,5,9'
    res = parse(data)
    assert res == [1, 3, 5, 9]
