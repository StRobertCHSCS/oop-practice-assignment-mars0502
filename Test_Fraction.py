import unittest
import Fraction as FractionClass

class TestFraction(unittest.TestCase):

    def setUp(self):
        self.fraction1 = FractionClass.Fraction(3,4)
        self.fraction2 = FractionClass.Fraction(2,3)

        self.fraction3 = FractionClass.Fraction(1,4)


    def test_instance_creation(self):
        self.assertIsInstance(self.fraction1, FractionClass.Fraction)

    def test_instance_creation_0Denom(self):
        with self.assertRaises(ValueError):
            self.fractionError = FractionClass.Fraction(1,0)

    def test_get_numerator(self):
        self.assertEquals(self.fraction1.get_numerator(), 3)

    def test_get_denominator(self):
        self.assertEquals(self.fraction1.get_denominator(), 4)

    def test_set_denominatorBasic(self):
        self.fraction1.set_denominator(8)
        self.assertEquals(self.fraction1.__str__(), "3/8")

    def test_set_denominator0(self):
        with self.assertRaises(ValueError):
            self.fraction1.set_denominator(0)

    def test_str(self):
        self.assertEquals(self.fraction1.__str__(), "3/4")

    def test_add(self):
        self.fraction1.add(self.fraction2)
        self.assertEquals(self.fraction1.__str__(), "17/12")

    def test_add_reduce(self):
        self.fraction3.add(self.fraction3)
        self.assertEquals(self.fraction3.__str__(), "1/2")



    def test_subtract(self):
        self.fraction1.subtract(self.fraction2)
        self.assertEquals(self.fraction1.__str__(), "1/12")


    def test_subtract_reduce(self):
        self.fraction1.subtract(self.fraction3)
        self.assertEquals(self.fraction1.__str__(), "1/2")


    def test_multiply(self):
        self.fraction1.multiply(self.fraction2)
        self.assertEquals(self.fraction1.__str__(), "1/2")





if __name__ == '__main__':
    unittest.main()



