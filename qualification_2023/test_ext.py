import unittest
from extension_strategique import *

class TestPlg6(unittest.TestCase):

    def test_simple_1(self):
        d = 3
        n = 4
        points_de_controles = [(1, 0), (2, 1), (2, -1), (0, 0)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 3)
    
    def test_simple_2(self):
        d = 4
        n = 5
        points_de_controles = [(0, 0), (0, 2), (1, 2), (2, 0), (2, 1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 4)

    def test_simple_3(self):
        d = 1
        n = 3
        points_de_controles = [(0, 0), (-1, 0), (1, 0)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 2)

    def test_n_is_1(self):
        d = 5
        n = 2
        points_de_controles = [(0, 0), (1, 1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 2)

    def test_no_out_1(self):
        d = 3
        n = 4
        points_de_controles = [(0, 0), (0, 2), (2, 2), (2, 1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 4)
    
    def test_no_out_2(self):
        d = 5
        n = 4
        points_de_controles = [(0, 0), (0, -2), (3, -4), (4, -3)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 4)
    
    def test_3_best_4(self):
        d = 5
        n = 5
        points_de_controles = [(0, 0), (0, -2), (1, -3), (2, -3), (4, -1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 3)

    def test_perf_1(self):
        d = 5
        n = 6
        points_de_controles = [(0, 0), (0, -2), (1, -3), (2, -3), (4, -1), (-1, 1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 3)

    def test_perf_2(self):
        d = 5
        n = 8
        points_de_controles = [(0, 0), (0, -3), (1, -3), (2, -3), (4, -1), (-1, 1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 3)

    def test_perf_3(self):
        d = 4
        n = 6
        points_de_controles = [(0, 0), (0, -3), (1, -3), (2, -3), (3, -2), (-1, 1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 4)

    def test_random_1(self):
        d = 3
        n = 4
        points_de_controles = [(0,0), (0, -2), (3, 0), (2, -2), (2, -1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 4)

    def test_random_2(self):
        d = 5
        n = 5
        points_de_controles = [(0, 0), (0, -2), (1, -3), (2, 0), (3, -1)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 4)

    def big_square(self):
        d = 40
        n = 5
        points_de_controles = [(0, 0), (2.82842712474619, 2.82842712474619), (-2.82842712474619, 2.82842712474619), (-2.82842712474619, -2.82842712474619), (2.82842712474619, -2.82842712474619)]
        self.assertEqual(aretes_minimales(d, n, points_de_controles), 4)


if __name__ == '__main__':
    unittest.main()