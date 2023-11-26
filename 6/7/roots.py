import pytest


def roots(a, b, c):
    if type(a) not in [int, float]:
        return None

    if type(b) not in [int, float]:
        return None

    if type(c) not in [int, float]:
        return None

    discr = b ** 2 - 4 * a * c

    if discr < 0:
        return None

    root1 = (-b - discr ** 0.5) / (2 * a)
    root2 = (-b + discr ** 0.5) / (2 * a)

    return root1, root2


def test_wrong_type_1():
    assert roots(None, 1, 1) is None


def test_wrong_type_2():
    assert roots(1, '1', 1) is None

def test_neg_discr():
    assert roots(1, 1, 1) is None

def test_equals_roots():
    root1, root2 = roots(1, 2, 1)
    assert root1 is not None and root1 == root2

def test_not_equals_roots_1():
    root1, root2 = roots(1, 3, -4)
    assert root1 is not None and root1 < root2

def test_not_equals_roots_2():
    root1, root2 = roots(1, 5, 3)
    assert root1 is not None and root1 < root2
