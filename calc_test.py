# Let's import pytest and unittest

import unittest
import pytest

from simple_calc import SimpleCalc

class Cacltest(unittest.TestCase):
    
    calc = SimpleCalc()

# assesertions to write our test cases
# we will use our basic calc example to write the tests first then the code

    def test_add(self):
        # naming convention is essential to have the word def in then name of the method
        self.assertEqual(self.calc.add(3,2) ,5) # if True test would pass
        #return num1 + num2

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3 ,2) ,1)

    def test_multi(self):
        self.assertEqual(self.calc.multi(2, 2), 4) #2x2 = 4

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2) # 6/3