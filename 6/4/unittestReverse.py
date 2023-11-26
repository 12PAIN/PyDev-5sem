import unittest


def reverse(s):
    if type(s) != str:
        raise TypeError(f'Expected str, got {type(s)}')

    return s[::-1]





class ReverseTest(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_one_char(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrom(self):
        self.assertEqual(reverse('abcba'), 'abcba')


    def test_regular(self):
        self.assertEqual(reverse('Привет!'), '!тевирП')

    def test_not_iterable(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_iterable(self):
        with self.assertRaises(TypeError):
            reverse(['1', '2', '3'])


if __name__ == '__main__':
    unittest.main()