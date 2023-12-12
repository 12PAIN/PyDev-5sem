from dateFunc import is_past_date
import unittest
import datetime


class TestIsPastDate(unittest.TestCase):
    def test_is_past_date_future_date(self):
        future_date = datetime.date.today() + datetime.timedelta(days=1)
        self.assertFalse(is_past_date(future_date))

    def test_is_past_date_current_date(self):
        current_date = datetime.date.today()
        self.assertFalse(is_past_date(current_date))

    def test_is_past_date_past_date(self):
        past_date = datetime.date.today() - datetime.timedelta(days=1)
        self.assertTrue(is_past_date(past_date))

    def test_is_past_date_invalid_date(self):
        invalid_date = "2022-05-32"
        with self.assertRaises(TypeError):
            is_past_date(invalid_date)


if __name__ == "__main__":
    unittest.main()
