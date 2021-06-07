import unittest

# enter your solution here
class TestJoinMethod(unittest.TestCase):
    def test_join_with_space(self):
        self.assertEquals(' '.join(['Python', '3.8']), 'Python 3.8')

    def test_join_with_comma(self):
        self.assertEquals(','.join(['open', 'high', 'low' , 'close']), 'open,high,low,close')

    def test_join_with_new_line_char(self):
        self.assertEquals('\n'.join(['open', 'high', 'low' , 'close']), 'open\nhigh\nlow\nclose')