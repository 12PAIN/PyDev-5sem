import pytest


def count_chars(s):

    if type(s) != str:
        raise TypeError

    charDict = {}

    for char in s:
        if char not in charDict.keys():
            charDict[char] = 0

        charDict[char] += 1

    return charDict


def test_wrong_type():
    with pytest.raises(TypeError):
        count_chars(42)


def test_empty():
    counts = count_chars('')
    assert counts == {}


def test_common():
    counts = count_chars('aabccc')
    assert counts == {'a': 2, 'b': 1, 'c': 3}