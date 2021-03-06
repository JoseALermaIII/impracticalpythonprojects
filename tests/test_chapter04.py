"""Test Chapter 4."""
import os
import unittest.mock
from io import StringIO
from random import Random
import src.ch04.practice.p1_hack_lincoln as hack_lincoln
import src.ch04.practice.p2_identify_cipher as identify_cipher
import src.ch04.practice.p2_identify_cipher_deco as identify_cipher_deco
import src.ch04.practice.p3_get_keys as get_keys
import src.ch04.practice.p4_generate_keys as generate_keys
import src.ch04.practice.p5_hack_route as hack_route
import src.ch04.challenge.c1_encode_route as encode_route
import src.ch04.challenge.c2_encode_rail as encode_rail


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
        keys = [[-1, -2], [-1, 2], [1, -2], [1, 2]]
        test_keys = hack_lincoln.keygen(2)
        self.assertListEqual(keys, test_keys)
        # Test odd key length
        keys = [[-1, -2, -3], [-1, -2, 3], [-1, 2, -3], [-1, 2, 3],
                [1, -2, -3], [1, -2, 3], [1, 2, -3], [1, 2, 3]]
        test_keys = hack_lincoln.keygen(3)
        self.assertListEqual(keys, test_keys)
        # Test big key length
        keys = [[-1, -2, -3, -4], [-1, -2, -3, 4], [-1, -2, 3, -4],
                [-1, -2, 3, 4], [-1, 2, -3, -4], [-1, 2, -3, 4],
                [-1, 2, 3, -4], [-1, 2, 3, 4], [1, -2, -3, -4],
                [1, -2, -3, 4], [1, -2, 3, -4], [1, -2, 3, 4],
                [1, 2, -3, -4], [1, 2, -3, 4], [1, 2, 3, -4], [1, 2, 3, 4]]
        test_keys = hack_lincoln.keygen(4)
        self.assertListEqual(keys, test_keys)

    def test_decode_route(self):
        """Test decode_route."""
        message = "this is supposed to be a super secret message stop"
        # Test a two column key.
        ciphertext = "message super be supposed this is to a secret stop"
        keys = [-1, 2]
        test_message = hack_lincoln.decode_route(keys, ciphertext.split())
        self.assertListEqual(message.split(), test_message)
        # Test a five column key.
        ciphertext = "this a super is secret supposed to message stop be"
        keys = [1, -2, -3, 4, -5]
        test_message = hack_lincoln.decode_route(keys, ciphertext.split())
        self.assertListEqual(message.split(), test_message)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_hack_route(self, mock_stdout):
        """Test hack_route."""
        with open(os.path.normpath('tests/data/ch04/hack_lincoln_func.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        ciphertext = "message super be supposed this is to a secret stop"
        hack_lincoln.hack_route(ciphertext)
        self.assertEqual(mock_stdout.getvalue(), file_data)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        hack_lincoln.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/main/hack_lincoln.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
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
        # Test blank line.
        ciphertext = ' '
        self.assertTrue(identify_cipher.identify_cipher(ciphertext, 0.0))
        # Test 12 most frequent English letters.
        ciphertext = 'etaoinshrdlu'
        self.assertTrue(identify_cipher.identify_cipher(ciphertext, 1))

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

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        # Test hard-coded cipher.
        identify_cipher.main()
        # Test inputted cipher.
        # Used key of 11 in Al Sweigart's Cracking Codes with Python
        # transpositionEncrypt.py
        ciphertext = """ok  oxt th hnltso iehtaeeehhrpcie  n  ru
                        ikgmnbtmetfcsh iiwye ik tsngo  tv s te  sfheuelr fbhoe pvaatauou s
                        eyietcerdisn gn"""
        identify_cipher.main(ciphertext)
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/main/identify_cipher_deco.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestIdentifyCipherDeco(unittest.TestCase):
    """Test Identify Cipher Deco."""

    def test_identify(self):
        """Test identify."""
        deco_func = identify_cipher_deco.identify(threshold=0.8)
        # Test letter transposition cipher.
        # Used key of 11 in Al Sweigart's Cracking Codes with Python
        # transpositionEncrypt.py
        ciphertext = """ok  oxt th hnltso iehtaeeehhrpcie  n  ru
                        ikgmnbtmetfcsh iiwye ik tsngo  tv s te  sfheuelr fbhoe pvaatauou s
                        eyietcerdisn gn"""
        self.assertTrue(deco_func(ciphertext))
        # Test letter substitution cipher.
        # Used key of FRSDBTVXANQJWLYUPGCEKZIOHM in Al Sweigart's
        # Cracking Codes with Python simpleSubCipher.py
        deco_func = identify_cipher_deco.identify(threshold=0.35)
        ciphertext = """ylb eiy rksqjb wh cxyb exgbb tykg cxke exb dyyg tazb cao uasq ku
                        ceasqc cbzbl bavxe jfh exbw cegfavxe lalb ebl f rav tfe xbl"""
        self.assertTrue(deco_func(ciphertext))

    def test_is_transposition(self):
        """Test that it can also identify a letter transposition cipher."""
        # Used key of 11 in Al Sweigart's Cracking Codes with Python
        # transpositionEncrypt.py
        ciphertext = """ok  oxt th hnltso iehtaeeehhrpcie  n  ru
                ikgmnbtmetfcsh iiwye ik tsngo  tv s te  sfheuelr fbhoe pvaatauou s
                eyietcerdisn gn"""
        self.assertTrue(identify_cipher_deco.is_transposition(ciphertext))

    def test_is_substitution(self):
        """Test that it can also identify a letter substitution cipher."""
        # Used key of FRSDBTVXANQJWLYUPGCEKZIOHM in Al Sweigart's
        # Cracking Codes with Python simpleSubCipher.py
        ciphertext = """ylb eiy rksqjb wh cxyb exgbb tykg cxke exb dyyg tazb cao uasq ku
                ceasqc cbzbl bavxe jfh exbw cegfavxe lalb ebl f rav tfe xbl"""
        self.assertTrue(identify_cipher_deco.is_substitution(ciphertext))


class TestGetKeys(unittest.TestCase):
    """Test Get Keys."""

    def test_key_to_dict(self):
        """Test key_to_dict."""
        # Test even key.
        key = [1, -2, -3, 4]
        answer = {1: 'up', 2: 'down', 3: 'down', 4: 'up'}
        test_dict = get_keys.key_to_dict(key)
        self.assertDictEqual(answer, test_dict)
        # Test odd key.
        key = [1, -2, -3, 4, -5]
        answer = {1: 'up', 2: 'down', 3: 'down', 4: 'up', 5: 'down'}
        test_dict = get_keys.key_to_dict(key)
        self.assertDictEqual(answer, test_dict)
        # Test positive key.
        key = [1, 2, 3, 4]
        answer = {1: 'up', 2: 'up', 3: 'up', 4: 'up'}
        test_dict = get_keys.key_to_dict(key)
        self.assertDictEqual(answer, test_dict)
        # Test negative key.
        key = [-1, -2, -3, -4]
        answer = {1: 'down', 2: 'down', 3: 'down', 4: 'down'}
        test_dict = get_keys.key_to_dict(key)
        self.assertDictEqual(answer, test_dict)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_get_keys(self, mock_stdout):
        """Test get_keys."""
        # Mock user input.
        with unittest.mock.patch('builtins.input',
                                 side_effect=[4, 1, -2, -3, 4]):
            test_keys = get_keys.get_keys()
        # Test return value.
        answer = [1, -2, -3, 4]
        self.assertListEqual(answer, test_keys)
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/get_keys_func.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        # Mock user input.
        with unittest.mock.patch('builtins.input',
                                 side_effect=[5, 1, -2, -3, 4, -5]):
            get_keys.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/main/get_keys.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestGenerateKeys(unittest.TestCase):
    """Test Generate Keys."""

    def test_generate_keys(self):
        """Test generate_keys."""
        # Test small key length
        keys = [(-1, 2), (1, -2), (1, 2), (-1, -2)]
        test_keys = generate_keys.generate_keys(2)
        self.assertListEqual(keys, test_keys)
        # Test odd key length
        keys = [(1, 2, -3), (-1, 2, 3), (-1, -2, 3), (1, -2, -3),
                (1, -2, 3), (-1, -2, -3), (-1, 2, -3), (1, 2, 3)]
        test_keys = generate_keys.generate_keys(3)
        self.assertListEqual(keys, test_keys)
        # Test big key length
        keys = [(-1, 2, -3, 4), (-1, -2, 3, 4), (-1, -2, 3, -4),
                (-1, 2, 3, -4), (-1, -2, -3, -4), (1, -2, -3, 4),
                (1, -2, 3, 4), (1, 2, -3, 4), (1, 2, 3, 4), (1, -2, 3, -4),
                (1, -2, -3, -4), (1, 2, -3, -4), (-1, -2, -3, 4),
                (1, 2, 3, -4), (-1, 2, 3, 4), (-1, 2, -3, -4)]
        test_keys = generate_keys.generate_keys(4)
        self.assertListEqual(keys, test_keys)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        generate_keys.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/main/generate_keys.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestHackRoute(unittest.TestCase):
    """Test Hack Route."""

    def test_decode_route(self):
        """Test decode_route."""
        message = "this is supposed to be a super secret message stop"
        # Test a two column key.
        ciphertext = "message super be supposed this is to a secret stop"
        keys = {1: 'down', 2: 'up'}
        test_message = hack_route.decode_route(keys, ciphertext.split())
        self.assertListEqual(message.split(), test_message)
        # Test a five column key.
        ciphertext = "this a super is secret supposed to message stop be"
        keys = {1: 'up', 2: 'down', 3: 'down',
                4: 'up', 5: 'down'}
        test_message = hack_route.decode_route(keys, ciphertext.split())
        self.assertListEqual(message.split(), test_message)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_hack_route(self, mock_stdout):
        """Test hack_route."""
        with open(os.path.normpath('tests/data/ch04/hack_route_func.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        ciphertext = "this a super is secret supposed to message stop be"
        hack_route.hack_route(ciphertext, 5)
        self.assertEqual(mock_stdout.getvalue(), file_data)
        # Test uppercase ciphertext
        mock_stdout.truncate(0)  # Truncate StringIO to length 0.
        mock_stdout.seek(0)  # Reset position to 0. Python 3.x only.
        with open(os.path.normpath('tests/data/ch04/hack_route_func2.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        ciphertext = "MESSAGE SUPER BE SUPPOSED THIS IS TO A SECRET STOP"
        hack_route.hack_route(ciphertext, 2)
        self.assertEqual(mock_stdout.getvalue(), file_data)
        # Test substitution cipher.
        # Used key of FRSDBTVXANQJWLYUPGCEKZIOHM in Al Sweigart's
        # Cracking Codes with Python simpleSubCipher.py
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        ciphertext = """ylb eiy rksqjb wh cxyb exgbb tykg cxke exb dyyg tazb cao uasq ku
                ceasqc cbzbl bavxe jfh exbw cegfavxe lalb ebl f rav tfe xbl"""
        hack_route.hack_route(ciphertext, 5)
        output = 'Hey, bub, I can\'t help you with substitution ciphers.\n'
        self.assertEqual(mock_stdout.getvalue(), output)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        hack_route.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/main/hack_route.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestEncodeRoute(unittest.TestCase):
    """Test Encode Route."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random()

    def test_format_plaintext(self):
        """Test format_plaintext."""
        # Check that it converts uppercase to lowercase.
        plaintext = 'This is only a TEST'
        cleantext = encode_route.format_plaintext(plaintext)
        self.assertEqual('this is only a test'.split(), cleantext)
        # Check that it removes punctuation.
        plaintext = 'So, hi. How are you? I\'m fine; thanks.'
        cleantext = encode_route.format_plaintext(plaintext)
        self.assertEqual('so hi how are you im fine thanks'.split(), cleantext)

    def test_replace_words(self):
        """Test replace_words."""
        # Test default dictionary.
        plaintext = 'my birthday is april 29'
        cleantext = ' '.join(encode_route.replace_words(plaintext.split()))
        self.assertEqual('my birthday is clayton add', cleantext)
        plaintext = 'cry me a river'
        cleantext = ' '.join(encode_route.replace_words(plaintext.split()))
        self.assertEqual('cry me a hickory', cleantext)
        plaintext = 'nothing to replace here'
        cleantext = ' '.join(encode_route.replace_words(plaintext.split()))
        self.assertEqual(plaintext, cleantext)
        # Test custom dictionary.
        plaintext = """My birthday is noon tomorrow We're going to a venue by
            the corner of floormart to celebrate. Don't bring a cheap gift -
            like beer"""
        code_words = {'noon': 'april', 'tomorrow': '29', 'venue': 'river',
                      'corner': 'gulf', 'floormart': 'mexico',
                      'beer': 'batteries'}
        cleantext = ' '.join(encode_route.replace_words(plaintext.split(),
                                                        code_words))
        answertext = ('My birthday is april 29 We\'re going to a river by '
                      'the gulf of mexico to celebrate. Don\'t bring a cheap gift - '
                      'like batteries')
        self.assertEqual(answertext, cleantext)

    @unittest.mock.patch('src.ch04.challenge.c1_encode_route.choice')
    @unittest.mock.patch('src.ch04.challenge.c1_encode_route.DICTIONARY_FILE_PATH', 'tests/data/ch04/dictionary.txt')
    def test_fill_dummy(self, mock_choice):
        """Test fill_dummy."""
        mock_choice._mock_side_effect = self.random.choice
        self.random.seed(361)  # Set seed here for test consistency.
        # Test default dummy_word list.
        plaintext = 'this is a'
        testlist = encode_route.fill_dummy(plaintext.split(), [3, 6])
        answerlist = ['this', 'is', 'a', 'full', 'filler', 'fuller']
        self.assertListEqual(answerlist, testlist)
        # Test custom dummy_word list.
        plaintext = 'what is the'
        dummylist = ['matter', 'matters', 'mattered', 'mattering']
        testlist = encode_route.fill_dummy(plaintext.split(), [2, 4], dummylist)
        answerlist = ['what', 'is', 'the', 'mattering']
        self.assertListEqual(answerlist, testlist)

    @unittest.mock.patch('src.ch04.challenge.c1_encode_route.choice')
    @unittest.mock.patch('src.ch04.challenge.c1_encode_route.DICTIONARY_FILE_PATH', 'tests/data/ch04/dictionary.txt')
    def test_encode_route(self, mock_choice):
        """Test encode_route."""
        mock_choice._mock_side_effect = self.random.choice
        self.random.seed(211)
        plaintext = 'This is supposed to be a super secret message.'
        # Test 2 x 5 route table.
        keys = [1, -2, 3, -4, 5]
        cipherlist = encode_route.encode_route(plaintext, keys, 2)
        answerlist = ['this', 'a', 'super', 'is', 'supposed', 'secret',
                      'message', 'to', 'be', 'full']
        self.assertListEqual(answerlist, cipherlist)
        # Test 5 x 2 route table.
        keys = [1, -2]
        cipherlist = encode_route.encode_route(plaintext, keys, 5)
        answerlist = ['this', 'supposed', 'be', 'super', 'message',
                      'filled', 'secret', 'a', 'to', 'is']
        self.assertListEqual(answerlist, cipherlist)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    @unittest.mock.patch('src.ch04.challenge.c1_encode_route.choice')
    @unittest.mock.patch('src.ch04.challenge.c1_encode_route.DICTIONARY_FILE_PATH', 'tests/data/ch04/dictionary.txt')
    def test_main(self, mock_choice, mock_stdout):
        """Test demo main function."""
        mock_choice._mock_side_effect = self.random.choice
        self.random.seed(555)
        encode_route.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/main/encode_route.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestEncodeRail(unittest.TestCase):
    """Test Encode Rail."""

    def test_split_rails(self):
        """Test split_rails."""
        # t . . . i . . . l . . . e . . . e . . . g .
        # . h . s . s . n . y . t . s . m . s . a . e
        # . . i . . . o . . . a . . . t . . . s . . .
        plaintext = 'thisisonlyatestmessage'
        testtext = encode_rail.split_rails(plaintext)
        ciphertext = 'tileeghssnytsmsaeioats'
        self.assertEqual(testtext, ciphertext)

    def test_encode_rail(self):
        """Test encode_rail."""
        message = ('The Eagle landed in the Sea of Tranquility on July 20, '
                   '1969.')
        # Test default split.
        testtext = encode_rail.encode_rail(message)
        ciphertext = ('talet etqin y9heg eaddn hsafr nulto jl216 elnie oaiyu '
                      '09')
        self.assertEqual(testtext, ciphertext)
        # Test custom split.
        testtext = encode_rail.encode_rail(message, 8)
        ciphertext = 'taletetq iny9hege addnhsaf rnultojl 216elnie oaiyu09'
        self.assertEqual(testtext, ciphertext)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        encode_rail.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch04/main/encode_rail.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


if __name__ == '__main__':
    unittest.main()
