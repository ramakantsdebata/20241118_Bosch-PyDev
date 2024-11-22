import unittest
from unittest.mock import MagicMock, patch, Mock

import sys
sys.path.insert(0, "..\\")
from _25_UnitTesting._02_MockTests.src._01_simpleCalculator import Calculator
import _25_UnitTesting._02_MockTests

class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('_25_UnitTesting._02_MockTests.src._01_simpleCalculator.Calculator')
    def test_something(self, MockClass):
        instance = MockClass()
        instance.add.return_value = 22
        print(instance.add())
        self.assertEqual(22, instance.add())

        # Check that MockClass is a mock object replacing Calculator in the module
        self.assertIs(MockClass, _25_UnitTesting._02_MockTests.src._01_simpleCalculator.Calculator)

    @unittest.mock.patch('_25_UnitTesting._02_MockTests.src._01_simpleCalculator.Calculator.add2', return_value=99)
    # Mocking the method Calculator.add2(a, b)
    def test_add2_mock(self, func):
        # Method 1
        # self.assertEqual(99, func(3, 4))

        # Method 2
        ins = Calculator(2, 3)
        print("add [2, 3] -->", ins.add())
        print("add2(5, 6) -->", ins.add2(5, 6))
        self.assertEqual(99, ins.add2(7, 8))

    @unittest.mock.patch('_25_UnitTesting._02_MockTests.src._01_simpleCalculator.Calculator.mul', return_value=75)
    def test_mul_mock(self, func):
        ins = Calculator(2, 3)
        print("add2(5, 6)   -->", ins.add2(5, 6))       # add2 is not mocked here.
        print("mul() [2, 3] -->", ins.mul())                 # mul is mocked here.
        self.assertEqual(75, ins.mul())

if __name__ == '__main__':
    unittest.main()



