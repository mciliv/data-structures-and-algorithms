from min_moves import *
import unittest

class TestNewPositions(unittest.TestCase):
    def test_new_positions(self):
        self.assertEqual(new_positions(PIECE_MOVES['King'], (0, 0), set()),
            {(0, 1), (1, 1), (1, 0)})
        self.assertEqual(new_positions(PIECE_MOVES['Knight'], (0, 0), set()),
            {(1, 2), (2, 1)})
        self.assertEqual(new_positions(PIECE_MOVES['Bishop'], (0, 0), set()),
            {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)})

class TestMinMoves(unittest.TestCase):
   def test_all_same_position(self):
       for i in range(BOARD_DIM):
           for j in range(BOARD_DIM):
               self.assertEqual(min_moves('King', (i, j), (i, j)), 0)
               self.assertEqual(min_moves('Knight', (i, j), (i, j)), 0)
               self.assertEqual(min_moves('Bishop', (i, j), (i, j)), 0)

   def test_varying_placements(self):
       self.assertEqual(min_moves('King', (0, 0), (2, 1)), 2)
       self.assertEqual(min_moves('Knight', (0, 0), (2, 1)), 1)
       self.assertEqual(min_moves('Bishop', (0, 0), (2, 1)), None)

       self.assertEqual(min_moves('King', (1, 0), (2, 1)), 1)
       self.assertEqual(min_moves('Knight', (1, 0), (2, 1)), 2)
       self.assertEqual(min_moves('Bishop', (1, 0), (2, 1)), 1)

       self.assertEqual(min_moves('King', (1, 0), (3, 6)), 6)
       self.assertEqual(min_moves('Knight', (1, 0), (3, 6)), 4)
       self.assertEqual(min_moves('Bishop', (1, 0), (3, 6)), 2)

       self.assertEqual(min_moves('King', (0, 0), (7, 7)), 7)
       self.assertEqual(min_moves('Knight', (0, 0), (7, 7)), 6)
       self.assertEqual(min_moves('Bishop', (0, 0), (7, 7)), 1)

       self.assertEqual(min_moves('King', (0, 1), (6, 0)), 6)
       self.assertEqual(min_moves('Knight', (0, 1), (6, 0)), 3)
       self.assertEqual(min_moves('Bishop', (0, 1), (6, 0)), None)

       self.assertEqual(min_moves('King', (0, 1), (7, 0)), 7)
       self.assertEqual(min_moves('Knight', (0, 1), (7, 0)), 4)
       self.assertEqual(min_moves('Bishop', (0, 1), (7, 0)), 2)

       self.assertEqual(min_moves('King', (0, 0), (7, 0)), 7)
       self.assertEqual(min_moves('Knight', (0, 0), (7, 0)), 5)
       self.assertEqual(min_moves('Bishop', (0, 0), (7, 0)), None)

   def test_varying_placements_reverse(self):
       self.assertEqual(min_moves('King', (2, 1), (0, 0)), 2)
       self.assertEqual(min_moves('Knight', (2, 1), (0, 0)), 1)
       self.assertEqual(min_moves('Bishop', (2, 1), (0, 0)), None)

       self.assertEqual(min_moves('King', (2, 1), (1, 0)), 1)
       self.assertEqual(min_moves('Knight', (2, 1), (1, 0)), 2)
       self.assertEqual(min_moves('Bishop', (2, 1), (1, 0)), 1)

       self.assertEqual(min_moves('King', (3, 6), (1, 0)), 6)
       self.assertEqual(min_moves('Knight', (3, 6), (1, 0)), 4)
       self.assertEqual(min_moves('Bishop', (3, 6), (1, 0)), 2)

       self.assertEqual(min_moves('King', (7, 7), (0, 0)), 7)
       self.assertEqual(min_moves('Knight', (7, 7), (0, 0)), 6)
       self.assertEqual(min_moves('Bishop', (7, 7), (0, 0)), 1)

       self.assertEqual(min_moves('King', (6, 0), (0, 1)), 6)
       self.assertEqual(min_moves('Knight', (6, 0), (0, 1)), 3)
       self.assertEqual(min_moves('Bishop', (6, 0), (0, 1)), None)

       self.assertEqual(min_moves('King', (7, 0), (0, 1)), 7)
       self.assertEqual(min_moves('Knight', (7, 0), (0, 1)), 4)
       self.assertEqual(min_moves('Bishop', (7, 0), (0, 1)), 2)

       self.assertEqual(min_moves('King', (7, 0), (0, 0)), 7)
       self.assertEqual(min_moves('Knight', (7, 0), (0, 0)), 5)
       self.assertEqual(min_moves('Bishop', (7, 0), (0, 0)), None)

if __name__ == '__main__':
    unittest.main()
