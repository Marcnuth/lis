from lis.collections import objectize


def test_objectize():
    data = dict(a=1, b="c", c="999")
    obj = objectize(data)
    assert obj.a == data['a']
    assert obj.b == data['b']
    assert obj.c == data['c']
