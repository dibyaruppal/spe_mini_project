import unittest
import calculator
import math

class test_calculator(unittest.TestCase):

    def test_calculator_functions(self):
        # Test Square Root Function
        self.assertAlmostEqual(calculator.square_root_function(0),0)
        self.assertAlmostEqual(calculator.square_root_function(4),2)
        self.assertAlmostEqual(calculator.square_root_function(100),10)
        self.assertAlmostEqual(calculator.square_root_function(5),2.23606797749979)


        # Test natural logarithm Function
        self.assertAlmostEqual(calculator.logarithm_function(math.e),1)
        self.assertAlmostEqual(calculator.logarithm_function(1),0)
        self.assertAlmostEqual(calculator.logarithm_function(100),4.605170185988092)

        # Test Factorial Function
        self.assertAlmostEqual(calculator.factorial_function(1),1)
        self.assertAlmostEqual(calculator.factorial_function(0),1)
        self.assertAlmostEqual(calculator.factorial_function(4),24)
        self.assertAlmostEqual(calculator.factorial_function(5),120)

        # Test Power Function
        self.assertAlmostEqual(calculator.power_function(1,100),1)
        self.assertAlmostEqual(calculator.power_function(5,1),5)
        self.assertAlmostEqual(calculator.power_function(100,0),1)
        self.assertAlmostEqual(calculator.power_function(0,100),0)
        self.assertAlmostEqual(calculator.power_function(-2,2),4)

if __name__ == '__main__':
    unittest.main()

    