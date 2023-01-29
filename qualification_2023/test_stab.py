import unittest
from stabilisateurs import *

class TestStap(unittest.TestCase):

    def test_egal_0(self):

        n = [2, 12, 9, 7, 4]
        k = [1, 0, 2, 3, 1]
        p = [10, 10, 10, 10, 10]
        accroches = [
            [1, 2], 
            [1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8], 
            [1, 21, 43, 121, 767, 787, 966, 1003, 1599],
            [1,7, 42, 47, 97, 111, 145],
            [1, 4, 22, 24]
            ]
        for i in range(5):
            self.assertEqual(stabilite_maximale(n[i], k[i], p[i], accroches[i]), 0)

    def test_n_inf_12(self):
        n = [7, 8, 9, 9, 9, 12, 12]
        k = [2, 2, 2, 1, 3, 2, 3]
        sortie = [75, 91, 91, 91, 91, 148, 167]
        p = 100
        accroches = [
            [1, 2, 4, 8, 9, 9, 36],
            [1, 4, 12, 13, 15, 15, 19, 23],
            [1, 4, 12, 13, 15, 15, 19, 23, 36],
            [1, 4, 12, 13, 15, 15, 19, 23, 36],
            [1, 4, 12, 13, 15, 15, 19, 23, 36],
            [1, 3, 4, 7, 9, 11, 13, 13, 15, 19, 23, 24],
            [1, 3, 4, 7, 9, 11, 13, 13, 15, 19, 23, 24]
        ]
        for i in range(6):
            self.assertEqual(sortie[i], stabilite_maximale(n[i], k[i], p, accroches[i]))
        
    def test_stabilisateur(self):
        N = 9
        K = 2
        P = 10
        accroches = [1, 2, 3, 4, 5, 5, 5, 7, 9]
        
        # Appeler votre fonction ici
        result = stabilite_maximale(N, K, P, accroches)
        
        self.assertEqual(result, 9)

    def test_stabilisateur_different_inputs(self):
        N = 12
        K = 4
        P = 20
        accroches = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        
        # Appeler votre fonction ici
        result = stabilite_maximale(N, K, P, accroches)
        
        # Vérifier qu'elle renvoie le résultat attendu
        self.assertEqual(result, 33)

        

if __name__ == '__main__':
    unittest.main()