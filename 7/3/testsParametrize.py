from dateFunc import is_past_date
import pytest
import datetime


@pytest.mark.parametrize('n, expected', [(datetime.date(2023, 4, 23), True),
                                         (datetime.date(2013, 4, 23), True),
                                         (datetime.date(2043, 4, 23), False),
                                         (datetime.date(2023, 5, 23), True),
                                         (datetime.date(2023, 4, 25), True)])
def test_regular(n, expected):
    assert is_past_date(n) == expected


