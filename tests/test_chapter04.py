"""Test Chapter 4."""
import os
import unittest.mock
from io import StringIO
import src.ch04.practice.p1_hack_lincoln as hack_lincoln
import src.ch04.practice.p2_identify_cipher as identify_cipher


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

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_hack_route(self, mock_stdout):
        """Test hack_route."""
        with open(os.path.normpath('tests/data/ch04/hack_lincoln.txt'), 'r') as file:
            file_data = ''.join(file.readlines())
        ciphertext = "this is to supposed a be super secret stop message"
        hack_lincoln.hack_route(ciphertext)
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestIdentifyCipher(unittest.TestCase):
    """Test Identify Cipher."""

    def test_identify_cipher(self):
        """Test identify_cipher."""
        # Test a letter transposition cipher.
        # Used key of 11 in Al Sweigart's Cracking Codes with Python
        # transpositionEncrypt.py
        ciphertext = """ok  oxt th hnltso iehtaeeehhrpcie  n  ru 
        ikgmnbtmetfcsh iiwye ik tsngo  tv s te  sfheuelr fbhoe pvaatauou s 
        eyietcerdisn gn"""
        self.assertTrue(identify_cipher.identify_cipher(ciphertext, 0.8))
        # Test a letter substitution cipher.
        # Used key of FRSDBTVXANQJWLYUPGCEKZIOHM in Al Sweigart's
        # Cracking Codes with Python simpleSubCipher.py
        ciphertext = """ylb eiy rksqjb wh cxyb exgbb tykg cxke exb dyyg tazb cao uasq ku
        ceasqc cbzbl bavxe jfh exbw cegfavxe lalb ebl f rav tfe xbl"""
        self.assertFalse(identify_cipher.identify_cipher(ciphertext, 0.35))

    def test_is_transposition(self):
        """Test that it can also identify a letter transposition cipher."""
        # Used key of 11 in Al Sweigart's Cracking Codes with Python
        # transpositionEncrypt.py
        ciphertext = """ok  oxt th hnltso iehtaeeehhrpcie  n  ru
                ikgmnbtmetfcsh iiwye ik tsngo  tv s te  sfheuelr fbhoe pvaatauou s
                eyietcerdisn gn"""
        self.assertTrue(identify_cipher.is_transposition(ciphertext))

    def test_is_substitution(self):
        """Test that it can also identify a letter substitution cipher."""
        # Used key of FRSDBTVXANQJWLYUPGCEKZIOHM in Al Sweigart's
        # Cracking Codes with Python simpleSubCipher.py
        ciphertext = """ylb eiy rksqjb wh cxyb exgbb tykg cxke exb dyyg tazb cao uasq ku
                ceasqc cbzbl bavxe jfh exbw cegfavxe lalb ebl f rav tfe xbl"""
        self.assertTrue(identify_cipher.is_substitution(ciphertext))


if __name__ == '__main__':
    unittest.main()
