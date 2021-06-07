import unittest

# enter your solution here
class TestUpper(unittest.TestCase):
    def test_upper(self):
        self.assertEquals('summer'.upper(), 'SUMMER')
    
    def test_is_upper(self):
        self.assertTrue('SUMMER'.isupper())
        self.assertFalse('summer'.isupper())