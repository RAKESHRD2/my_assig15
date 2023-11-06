import unittest
from my_classes.subclass_2 import Subclass2

class TestSubclass2(unittest.TestCase):
    def test_do_something(self):
        obj = Subclass2(8)
        result = obj.do_something()
        self.assertEqual(result, 18)

    def test_zero_value(self):
        obj = Subclass2(0)
        result = obj.do_something()
        self.assertEqual(result, 10)

    # Add more test cases for Subclass2
