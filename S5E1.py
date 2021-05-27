import unittest

# enter your solution here
class TestSplitMethod(unittest.TestCase):
    def test_split_by_default(self):
        self.assertEquals('Python Testing'.split(), ['Python', 'Testing'])

    def test_split_by_comma(self):
        self.assertEquals('open,high,low,close'.split(','), ['open', 'high', 'low', 'close'])

    def test_split_by_hash(self):
        self.assertEquals('summer#time#vibes'.split('#'), ['summer', 'time', 'vibes'])