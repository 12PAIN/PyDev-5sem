import pytest
from Rectangle_Class import Rectangle


@pytest.fixture
def test_normal_data():
    instance = Rectangle(2, 5)
    assert instance.get_area() == 10
    assert instance.get_perimetr() == 14


@pytest.fixture
def test_type_float():
    instance = Rectangle(0.1, 0.9)

    assert instance.get_area() == 0.09000000000000001
    assert instance.get_perimetr() == 2


@pytest.fixture
def test_zero():
    instance = Rectangle(0, 5)
    assert not instance.get_area()
    assert instance.get_perimetr() == 10


def test_one(test_zero):
    print("Test with sero side")


def test_two(test_normal_data):
    print("Test with normal data")


def test_three(test_type_float):
    print("Test with float type")
