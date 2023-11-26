import pytest
import re


def is_under_queen_attack(position, queen_position):
    if type(position) != str:
        raise TypeError

    if re.match('^[a-h][1-8]$', position) is None:
        raise ValueError('Ошибка в позиции')

    if type(queen_position) != str:
        raise TypeError

    if re.match('^[a-h][1-8]$', queen_position) is None:
        raise ValueError('Ошибка в позиции королевы')

    if position == queen_position:
        return True

    listedPos = list(position)
    listedQueenPos = list(queen_position)

    posCol = listedPos[0]
    queenPosCol = listedQueenPos[0]

    posRow = listedPos[1]
    queenPosRow = listedQueenPos[1]

    if posCol == queenPosCol or posRow == queenPosRow:
        return True

    underAttack = []
    colsList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    queenColIdx = colsList.index(queenPosCol) + 1
    posColIdx = colsList.index(posCol) + 1

    if abs(int(queenPosRow) - int(posRow)) == abs(queenColIdx - posColIdx):
        return True

    return False


def test_wrong_type():
    with pytest.raises(TypeError):
        is_under_queen_attack(None, 42)


def test_wrong_coordinate():
    with pytest.raises(ValueError):
        is_under_queen_attack("abc", "42")


def test_wrong_coordinate2():
    with pytest.raises(ValueError):
        is_under_queen_attack('c3', 'd4d')


def test_wrong_coordinate_out_of_bounds():
    with pytest.raises(ValueError):
        is_under_queen_attack("e1", "e9")


def test_attack_same_field():
    assert is_under_queen_attack("e5", "e5")


def test_attack_same_row():
    assert is_under_queen_attack("a1", "e1")


def test_attack_same_column():
    assert is_under_queen_attack("a1", "a8")


def test_attack_diagonal():
    assert is_under_queen_attack("b3", "e6")


def test_no_attack():
    assert not is_under_queen_attack("c4", "e5")
