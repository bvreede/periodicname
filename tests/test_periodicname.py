import unittest, os
import periodicname.periodicname as pn


class TestPeriodicName(unittest.TestCase):
    def test_make_word_list(self):
        # Test make_word_list for a predictable outcome
        sequence = pn.Sequencer("")
        self.assertEqual(sequence._make_word_list('DSSDDDSS',"thanksrenato"),['th','a','n','ks','re','na','t','o'])
        # Testing error cases, including specific error message
        self.assertRaisesRegex(ValueError, "Length of sequence", sequence._make_word_list, "", "String")
        self.assertRaisesRegex(ValueError, "Length of sequence", sequence._make_word_list, "DDDDDDDDDSSSSDSDS", "String")



if __name__ == '__main__':
    unittest.main()