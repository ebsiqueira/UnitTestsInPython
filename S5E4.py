import unittest
from collections import Counter


class TestIsInstance(unittest.TestCase):

    def test_case_1(self):
        self.assertTrue(isinstance((), tuple))

    def test_case_2(self):
        self.assertTrue(isinstance([], list))

    def test_case_3(self):
        self.assertTrue(isinstance({}, dict))

    def test_case_4(self):
        cnt = Counter()
        self.assertTrue(isinstance(cnt, Counter))

    def test_case_5(self):
        var1 = 4
        self.assertTrue(isinstance(var1, int))

    def test_case_6(self):
        var2 = 4
        self.assertTrue(isinstance(var2, int))