import unittest, os
import periodicname.periodicname as pn


class TestPeriodicName(unittest.TestCase):
    def setUp(self):
        self.sequence = pn.ElementalWord("testword")

    def test_make_word_list(self):
        """Testing make_word_list to correctly split a word."""
        self.assertEqual(self.sequence._make_word_list('DSSDDDSS',"thanksrenato"),['th','a','n','ks','re','na','t','o'])

        # Testing error cases, including specific error message
        with self.assertRaisesRegex(ValueError, "Length of sequence"):
            self.sequence._make_word_list("", "String")
        with self.assertRaisesRegex(ValueError, "Length of sequence"):
            self.sequence._make_word_list("DDDDDDDDDSSSSDSDS", "String")

    def test_periodic_name(self):
        """Testing that the package correctly assigns elements to a sentence."""
        self.assertEqual(pn.periodic_name("Hello World"),[['He', '', '', 'O'], ['W', 'O', '', '', '']])
    






if __name__ == '__main__':
    unittest.main()