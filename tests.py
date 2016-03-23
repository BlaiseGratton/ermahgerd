import unittest
from ermahgerd import ermahgerd


class TestErmahgerdOutput(unittest.TestCase):

    def test_1(self):
        people = ermahgerd("people")
        purple = ermahgerd("purple")
        self.assertEqual(people, purple)

    def test_2(self):
        spicy_pork = ermahgerd("spicy pork")
        special_park = ermahgerd("special park")
        self.assertEqual(spicy_pork, special_park)

    def test_3(self):
        self.assertEqual("erf", ermahgerd("if"))

    def test_4(self):
        self.assertEqual("ceryerter", ermahgerd("coyote"))

    def test_5(self):
        self.assertEqual("lertter", ermahgerd("little"))

if __name__ == '__main__':
    unittest.main()
