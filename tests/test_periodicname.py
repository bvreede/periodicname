import unittest, os
import periodicname.periodicname as pn
import periodicname.periodicelements as pe


class TestPeriodicName(unittest.TestCase):
    def setUp(self):
        self.sequence = pn.ElementalWord("Hello World") # instantiate to be able to use the class functions

    def test_make_sequences(self):
        """Test if the object sequences is correctly generated"""
        self.assertEqual(self.sequence.sequences[:3],['SSSSSSSSSSS', 'SSSSSSSSSD', 'SSSSSSSSDS'])

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
        helloworld = pn.periodic_name("Hello World")

        # Test that the right elements are chosen
        self.assertEqual(helloworld,[['He', '', '', 'O'], ['W', 'O', '', '', '']])
        
        # Test that the sentence is split into separate words
        self.assertEqual(len(helloworld),2)
     

class TestPeriodicElements(unittest.TestCase):
    def test_get_elements(self):
        """Test that the periodic elements can be correctly loaded"""
        symbols = pe.get_elements()
        self.assertEqual(len(symbols),118)




if __name__ == '__main__':
    unittest.main()