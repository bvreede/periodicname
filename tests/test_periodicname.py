import unittest, os
import periodicname.periodicname as pn





class TestPeriodicNames(unittest.TestCase):
    def test_makename(self):
        # Test makename for a predictable outcome
        self.assertEqual(pn._makename('DSSDDDSS',"thanksrenato"),['th','a','n','ks','re','na','t','o'])
        # Testing error cases in makename, including specific error message
        self.assertRaisesRegex(ValueError, "Length of sequence", pn._makename, "", "String")
        self.assertRaisesRegex(ValueError, "Length of sequence", pn._makename, "DDDDDDDDDSSSSDSDS", "String")



if __name__ == '__main__':
    unittest.main()