import unittest
from permutate import permutate

class TestPermutation(unittest.TestCase):
    def test_non_string_raises_error(self):
        with self.assertRaises(Exception) as e:
            permutate(123)

    def test_empty_character(self):
        permutations = permutate('')
        self.assertListEqual(permutations, [''])
        self.assertEqual(len(permutations), 1)

    def test_single_character(self):
        permutations = permutate('a')
        self.assertListEqual(permutations, ['a'])
        self.assertEqual(len(permutations), 1)

    def test_unique_characters(self):
        permutations = permutate('at')
        self.assertListEqual(permutations, ['at', 'ta'])
        self.assertEqual(len(permutations), 2)

        permutations = permutate('bike')
        self.assertListEqual(
            permutations,
            [
                'bike',
                'biek',
                'bkie',
                'bkei',
                'beik',
                'beki',
                'ibke',
                'ibek',
                'ikbe',
                'ikeb',
                'iebk',
                'iekb',
                'kbie',
                'kbei',
                'kibe',
                'kieb',
                'kebi',
                'keib',
                'ebik',
                'ebki',
                'eibk',
                'eikb',
                'ekbi',
                'ekib'
            ]
        )
        self.assertEqual(len(permutations), 24)

    def test_repeating_characters(self):
        permutations = permutate('aa')
        self.assertListEqual(permutations, ['aa'])
        self.assertEqual(len(permutations), 1)

        permutations = permutate('book')
        self.assertListEqual(
            permutations,
            [
                'book', 'boko', 'bkoo', 'obok', 'obko', 'oobk', 'ookb', 'okbo', 'okob', 'kboo', 'kobo', 'koob'
            ]
        )
        self.assertEqual(len(permutations), 12)

        permutations = permutate('mississippi')
        self.assertEqual(len(permutations), 34650)
