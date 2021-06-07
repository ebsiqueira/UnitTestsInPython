import unittest

class TestLstripMethod(unittest.TestCase):
    def test_starts_with_one_whitespace(self):
        self.assertEquals(' test'.lstrip(), 'test')

    def test_starts_and_ends_with_whitespace(self):
        self.assertEquals(' test '.lstrip(), 'test ')

class TestStripMethod(unittest.TestCase):
    def test_starts_and_ends_with_whitespace(self):
        self.assertEquals(' test '.strip(), 'test')

    def test_no_whitespace(self):
        self.assertEquals('test'.strip(), 'test')

class TestRstripMethod(unittest.TestCase):
    def test_starts_and_ends_with_whitespace(self):
        self.assertEquals(' test '.rstrip(), ' test')

    def test_ends_with_one_whitespace(self):
        self.assertEquals('test '.rstrip(), 'test')
