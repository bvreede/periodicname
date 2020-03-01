import unittest, os
import periodicname.periodicname as sequence





class TestPeriodicNames(unittest.TestCase):
    def test_makename(self):
        # Test makename for a predictable outcome
        self.assertEqual(sequence.makename('DSSDDDSS',"thanksrenato"),['th','a','n','ks','re','na','t','o'])
        # Testing error cases in makename, including specific error message
        self.assertRaisesRegex(ValueError, "Length of sequence", sequence.makename, "", "String")
        self.assertRaisesRegex(ValueError, "Length of sequence", sequence.makename, "DDDDDDDDDSSSSDSDS", "String")



if __name__ == '__main__':
    unittest.main()