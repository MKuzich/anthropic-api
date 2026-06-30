import unittest
from main import calculate_pi

class TestCalculatePi(unittest.TestCase):

    def test_pi_to_5th_decimal(self):
        """Test that calculate_pi() returns pi rounded to 5 decimal places."""
        self.assertEqual(calculate_pi(), 3.14159)

    def test_return_type_is_float(self):
        """Test that calculate_pi() returns a float."""
        self.assertIsInstance(calculate_pi(), float)

    def test_pi_within_tolerance(self):
        """Test that calculate_pi() is within 0.000005 of the true value of pi."""
        import math
        self.assertAlmostEqual(calculate_pi(), math.pi, places=5)


if __name__ == "__main__":
    unittest.main()
