import unittest
import company as cp

class Testing_Employee(unittest.TestCase):

    def setUp(self):
        self.emp1 = cp.Employee('Aamir', 'Ayub', 3000)

    def test_string_exceptions(self):
        self.assertRaises(ValueError, cp.Employee.validate_string, 1)
        self.assertRaises(ValueError, cp.Employee.validate_string)
        self.assertRaises(ValueError, cp.Employee.validate_string, ' ')
        self.assertRaises(ValueError, cp.Employee.validate_string, '')
        self.assertRaises(ValueError, cp.Employee.validate_string, 'abc')

    def test_exceptions(self):
        self.assertRaises(ValueError, setattr, self.emp1, 'first', 1)
        self.assertRaises(ValueError, setattr, self.emp1, 'first', ' ')
        self.assertRaises(ValueError, setattr, self.emp1, 'first', '')
        self.assertRaises(ValueError, setattr, self.emp1, 'first', 'abc')

        self.assertRaises(ValueError, setattr, self.emp1, 'last', 1)
        self.assertRaises(ValueError, setattr, self.emp1, 'last', ' ')
        self.assertRaises(ValueError, setattr, self.emp1, 'last', '')
        self.assertRaises(ValueError, setattr, self.emp1, 'last', 'abc')

    def test_names(self):
        self.assertEqual(self.emp1.first, 'Aamir')
        self.assertEqual(self.emp1.last, 'Ayub')


if __name__ == '__main__':
    unittest.main()