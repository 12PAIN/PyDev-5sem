from choiceFunc import choice_one
import unittest
from unittest.mock import Mock, patch


class TestProductSelector(unittest.TestCase):

    def setUp(self):
        self.mock_cursor = Mock()
        self.mock_product_names = [('Apple',), ('Banana',), ('Cherry',)]

    @patch('choiceFunc.random.choice')
    def test_choice_one_returns_product(self, mock_choice):
        mock_choice.return_value = 'Banana'
        self.mock_cursor.fetchall.return_value = self.mock_product_names

        result = choice_one(self.mock_cursor)

        self.assertEqual(result, 'Banana')

    def test_choice_one_calls_fetchall(self):
        self.mock_cursor.fetchall.return_value = self.mock_product_names

        choice_one(self.mock_cursor)

        self.mock_cursor.fetchall.assert_called_once()

    @patch('choiceFunc.random.choice')
    def test_choice_one_randomly_chooses(self, mock_choice):
        mock_choice.side_effect = lambda x: x[0]
        self.mock_cursor.fetchall.return_value = self.mock_product_names

        result = choice_one(self.mock_cursor)

        mock_choice.assert_called_once_with(['Apple', 'Banana', 'Cherry'])
        self.assertEqual(result, 'Apple')


if __name__ == '__main__':
    unittest.main()
