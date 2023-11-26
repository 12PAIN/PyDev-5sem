import pytest

import pathFind
import io
import sys

@pytest.mark.parametrize("city1, city2", [(' ', ' '), ('Кемерово', 'Москва')])
def test_wrong_cities(monkeypatch, city1, city2):
    monkeypatch.setattr('sys.stdin', io.StringIO(f'{city1}\n{city2}'))
    with pytest.raises(ValueError):
        pathFind.main()

@pytest.mark.parametrize("fileNumber", list(range(1, 4)))
def test_by_files(monkeypatch, capsys, fileNumber):
    inputData = open(f'tests/input/input0{fileNumber}.txt', encoding='utf-8')
    expectedData = open(f'tests/output/output0{fileNumber}.txt', encoding='utf-8')

    monkeypatch.setattr('sys.stdin', io.StringIO(inputData.read()))
    pathFind.main()
    out, err = capsys.readouterr()
    assert err == ''
    assert out == expectedData.read() + '\n'
