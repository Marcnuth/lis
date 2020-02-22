from lis.streaming import streaming
from itertools import filterfalse


def test_streaming():
    data = range(20)

    res = streaming(data).filter(lambda x: x % 3).map(lambda x: x * x).reverse().sort().filterfalse(lambda x: x % 2).get_list()
    assert res == list(filterfalse(
        lambda x: x % 2,
        sorted(list(map(
            lambda x: x * x,
            filter(lambda x: x % 3, data)
        ))[::-1])
    ))
