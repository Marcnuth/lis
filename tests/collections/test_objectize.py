from lis.collections import objectize


def test_objectize():
    data = dict(a=1, b="c", c="999")
    obj = objectize(data)
    assert obj.a == data['a']
    assert obj.b == data['b']
    assert obj.c == data['c']


def test_recur_objectize():
    data = dict(a=1, b=dict(l2a=1111, l2b=dict(l3a="abdd", l3b=[1, 2, 3, 4])), c="999")
    obj = objectize(data)
    assert obj.a == data['a']
    assert obj.b.l2a == data['b']['l2a']
    assert obj.b.l2b.l3a == data['b']['l2b']['l3a']
    assert obj.b.l2b.l3b == data['b']['l2b']['l3b']
    assert obj.c == data['c']

    obj2 = objectize(data, recursive=False)
    assert obj2.a == data['a']
    assert obj2.b == data['b']
    assert isinstance(obj2.b, dict)
    assert obj2.c == data['c']
