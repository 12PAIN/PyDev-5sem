from fibo import fib
import pytest


@pytest.mark.parametrize('n, expected', [(1, 1), (2, 1), (3, 2), (4, 3), (5, 5),
                                         (6, 8), (7, 13), (8, 21), (9, 34), (10, 55)])
def test_regular(n, expected):
    assert fib(n) == expected
