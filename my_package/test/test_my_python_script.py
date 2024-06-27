import os.path
import unittest
import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname((__file__), '..', 'my_packae')))

from my_package.python_package.my_python_script import TestClass

class TestAddMethod(unittest.TestCase):
    def test_add_method(self):
        t = TestClass()
        self.assertEqual(t.add_method(1,2), 3)


if __name__ == '__main__' :
        print(sys.path)
        unittest()().main()