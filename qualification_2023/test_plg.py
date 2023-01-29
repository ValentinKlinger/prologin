import unittest
#from pas_malin_dromes import nb_pas_malin_drome
from greve_generale3 import trajets_retour
from stabilisateurs import *

class TestEx(unittest.TestCase):

    '''def test_pas_malin_dromes(self):
        n = 10
        mots = ['0KayAk0', '0KAYQk1', '0KayaK0', '4', '0123443210', 'qqqqqqqqqq', 'KK', 'HellO e0H']
        self.assertEqual(nb_pas_malin_drome(n, mots), 6)

    def test_pas_malin_dromes2(self):
        n =10
        mots = ['((àAooNAoo0  ẑ0', 'nnio,,EZE211 2oinn', 'kdle22122AZA', 'ù*$ap1pa221 AZOK', '1o2o1']
        self.assertEqual(nb_pas_malin_drome(n, mots), 3)
 
    def test_pas_malin_dromes3(self):
        n =10
        mots = ['((àAooZzAoo0  ẑ0', 'nnio,,EZE91 9oinn', 'kdle22122AZA', 'ù*$ap1pa221 AZOK', 'AZ199zoz1ZA']
        self.assertEqual(nb_pas_malin_drome(n, mots), 3)

    def test_pas_malin_dromes4(self):
        n =10
        mots = ['11', '99', '91', '454']
        self.assertEqual(nb_pas_malin_drome(n, mots), 3)

    def test_greve_generale(self):
        n = 4
        redirection = [[2, False],[0, False],[3, False],[0, False]]
        self.assertEqual(trajets_retour(n, redirection), '3 4 3 3')

    def test_greve_generale2(self):
        n = 5
        redirection = [[1, False], [2, False], [3, False], [4, False], [3, False]]
        self.assertEqual(trajets_retour(n, redirection), '5 4 3 2 2')

    def test_greve_generale3(self):
        n = 10
        redirection = [[1, False], [0, False], [3, False], [2, False], [5, False], [4, False], [7, False], [6, False], [9, False], [8, False]]
        self.assertEqual(trajets_retour(n, redirection), '2 2 2 2 2 2 2 2 2 2')'''

    def test_truc(self):
        n = 2
        k = 1
        p = 10
        accroches = [1, 2]
        self.assertEqual(stabilite_maximale(n, k, p, accroches), 0)
        
if __name__ == '__main__':
    unittest.main()

# 0 2 3 0
# 1 0 2 3 0
