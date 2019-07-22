"""Test Chapter 4."""
import unittest
import src.ch04.practice.p1_hack_lincoln as hack_lincoln


class TestHackLincoln(unittest.TestCase):
    """Test Hack Lincoln."""

    def test_get_factors(self):
        """Test get_factors."""
        # Test prime number
        factors = [1, 11]
        test_factors = hack_lincoln.get_factors(11)
        self.assertListEqual(factors, test_factors)
        # Test perfect square
        factors = [1, 2, 4]
        test_factors = hack_lincoln.get_factors(4)
        self.assertListEqual(factors, test_factors)
        # Test non-prime, non-perfect square
        factors = [1, 2, 4, 8, 16, 32]
        test_factors = hack_lincoln.get_factors(32)
        self.assertListEqual(factors, test_factors)

    def test_keygen(self):
        """Test keygen."""
        # Test small key length
        keys = [[-1, 2], [1, -2], [1, 2], [-1, -2]]
        test_keys = hack_lincoln.keygen(2)
        self.assertListEqual(keys, test_keys)
        # Test odd key length
        keys = [[1, 2, -3], [-1, 2, 3], [-1, -2, 3], [1, -2, -3],
                [1, -2, 3], [-1, -2, -3], [-1, 2, -3], [1, 2, 3]]
        test_keys = hack_lincoln.keygen(3)
        self.assertListEqual(keys, test_keys)
        # Test big key length
        keys = [[-1, 2, -3, 4], [-1, -2, 3, 4], [-1, -2, 3, -4],
                [-1, 2, 3, -4], [-1, -2, -3, -4], [1, -2, -3, 4],
                [1, -2, 3, 4], [1, 2, -3, 4], [1, 2, 3, 4], [1, -2, 3, -4],
                [1, -2, -3, -4], [1, 2, -3, -4], [-1, -2, -3, 4],
                [1, 2, 3, -4], [-1, 2, 3, 4], [-1, 2, -3, -4]]
        test_keys = hack_lincoln.keygen(4)
        self.assertListEqual(keys, test_keys)

    def test_decode_route(self):
        """Test decode_route."""
        message = "this is supposed to be a super secret message stop"
        # Test a two column key.
        ciphertext = "be to supposed is this a super secret message stop"
        keys = [-1, 2]
        test_message = hack_lincoln.decode_route(keys, ciphertext.split())
        self.assertListEqual(message.split(), test_message)
        # Test a five column key.
        ciphertext = "this is to supposed a be super secret stop message"
        keys = [1, -2, -3, 4, -5]
        test_message = hack_lincoln.decode_route(keys, ciphertext.split())
        self.assertListEqual(message.split(), test_message)


if __name__ == '__main__':
    unittest.main()