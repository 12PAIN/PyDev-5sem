import pytest

import filter_emails
import io
import sys


@pytest.mark.parametrize("fileNumber", list(range(0, 10)))
def test_emails(monkeypatch, capsys, fileNumber):
    inputData = open(f'tests/input/input0{fileNumber}.txt')
    expectedData = open(f'tests/output/output0{fileNumber}.txt')

    monkeypatch.setattr('sys.stdin', io.StringIO(inputData.read()))
    filter_emails.main()
    out, err = capsys.readouterr()
    assert err == ''
    assert out == expectedData.read() + '\n'
