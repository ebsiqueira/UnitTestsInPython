import unittest

# enter your solution here
class TestLower(unittest.TestCase):
    def test_lower(self):
        self.assertEquals('Joe.Smith@mail.com'.lower(), 'joe.smith@mail.com')
    
    def test_is_lower(self):
        self.assertTrue('joe.smith@mail.com'.islower)
        self.assertFalse('Joe.Smith@mail.com'.islower())