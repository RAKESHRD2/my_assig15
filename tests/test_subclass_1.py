import unittest
from my_classes.subclass_1 import Subclass1

class TestSubclass1(unittest.TestCase):
    def test_do_something(self):
        obj = Subclass1(5)
        result = obj.do_something()
        self.assertEqual(result, 10)

    def test_negative_value(self):
        obj = Subclass1(-3)
        result = obj.do_something()
        self.assertEqual(result, -6)

    # Add more test cases for Subclass1
