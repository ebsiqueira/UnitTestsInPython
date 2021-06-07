import unittest


class TestJoinMethod(unittest.TestCase):

    def test_join_with_space(self):
        self.assertEqual(' '.join(['Python', '3.8']), 'Python 3.8')

    def test_join_with_comma(self):
        actual = ','.join(['open', 'high', 'low', 'close'])
        expected = 'open,high,low,close'
        self.assertEqual(actual, expected)

    def test_join_with_new_line_char(self):
        actual = '\n'.join(['open', 'high', 'low', 'close'])
        expected = 'open\nhigh\nlow\nclose'
        self.assertEqual(actual, expected)
