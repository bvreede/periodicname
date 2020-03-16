import unittest, os
import periodicname.periodicname as pn


class TestPeriodicName(unittest.TestCase):
    def setUp(self):
        self.sequence = pn.Sequencer("testword")
        self.periodic = pn.PeriodicElements()

    def test_make_word_list(self):
        """Testing make_word_list to correctly split a word."""
        #self.sequence = pn.Sequencer("")
        self.assertEqual(self.sequence._make_word_list('DSSDDDSS',"thanksrenato"),['th','a','n','ks','re','na','t','o'])

        # Testing error cases, including specific error message
        with self.assertRaisesRegex(ValueError, "Length of sequence"):
            self.sequence._make_word_list("", "String")
        with self.assertRaisesRegex(ValueError, "Length of sequence"):
            self.sequence._make_word_list("DDDDDDDDDSSSSDSDS", "String")
    
    def test_word_to_symbol(self):
        """Test word_to_symbol to assign"""
        self.assertEqual(self.periodic.word_to_symbol(['B', 'Ar', 'Ba', 'Ra']),(['B', 'Ar', 'Ba', 'Ra'],7))






if __name__ == '__main__':
    unittest.main()