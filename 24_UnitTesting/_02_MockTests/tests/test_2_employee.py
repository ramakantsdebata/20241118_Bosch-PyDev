import unittest
from unittest.mock import patch, MagicMock
from _25_UnitTesting._02_MockTests.src._02_employee import Employee, Organisation
import _25_UnitTesting._02_MockTests.src._02_employee

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.emp1 = Employee(1, 'Pravin', 200)
        cls.emp2 = Employee(2, 'Rakesh', 100)

    def setUp(self):
        self.org = Organisation([self.emp1, self.emp2])

    @classmethod
    def tearDownClass(cls):
        pass

    def tearDown(self):
        pass

    def test_employee(self):
        sal1 = self.emp1.getSalary()
        self.assertEqual(sal1, 200)

    def test_empStrength(self):
        print("Emp count -->", self.org.getEmpCount())
        print("Strength check -->", self.org.checkEmployeeStrength())
        self.assertEqual('Waste of space', self.org.checkEmployeeStrength())

    @patch('_25_UnitTesting._02_MockTests.src._02_employee.Organisation.getEmpCount', return_value=235)
    def test_empStrength_with_mock(self, mock_getEmpCount):
        self.assertEqual('Just about right', self.org.checkEmployeeStrength())

    def test_empStrength_with_MagicMock(self):
        self.org.getEmpCount = MagicMock(return_value = 1010)
        self.assertEqual('Too congested', self.org.checkEmployeeStrength())
