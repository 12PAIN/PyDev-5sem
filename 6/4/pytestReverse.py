import unittest

import pytest


def reverse(s):
    if type(s) != str:
        raise TypeError(f'Expected str, got {type(s)}')

    return s[::-1]

def test_iterable():
    with pytest.raises(TypeError):
        reverse(['1','2','3'])
def test_not_iterable():
    with pytest.raises(TypeError):
        reverse(1)

def test_empty():
    assert reverse('') == ''

def test_one_char():
    assert reverse('a') == 'a'

def test_palindrom():
    assert reverse('abcba') == 'abcba'

def test_regular():
    assert reverse('Привет!') == '!тевирП'
