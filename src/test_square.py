from square import Square
from grid import Grid
import unittest

class Test_Square(unittest.TestCase):
    def setUp(self):
        # Placeholder grid 'tempgrid' passed on as an argument to the
        # Square, i.e. the Square's parent grid.
        self.tempgrid = Grid(1, 1, Square)

        self.testsquare = Square(1, 1, self.tempgrid)

    def test_location(self):
        self.assertEqual(Square(0, 0, self.tempgrid).location(), (0,0))
        self.assertEqual(Square(1, 2, self.tempgrid).location(), (1,2))
        self.assertEqual(Square(-1, -2, self.tempgrid).location(), (-1,-2))

    def test_mine_true(self):
        self.assertTrue(Square(1, 1, self.tempgrid, True).mine())
    def test_mine_false(self):
        self.assertFalse(Square(1, 1, self.tempgrid, False).mine())
    def test_mine_default(self):
        self.assertFalse(Square(1, 1, self.tempgrid).mine())

    def test_set_dangerlevel(self):
        self.assertEqual(self.testsquare.dangerlevel(), 0)
        self.testsquare.set_dangerlevel(10)
        self.assertEqual(self.testsquare.dangerlevel(), 10)
    
    def test_increment_dangerlevel_once(self):
        self.testsquare.set_dangerlevel(0)
        self.assertEqual(self.testsquare.dangerlevel(), 0)
        self.testsquare.increment_dangerlevel()
        self.assertEqual(self.testsquare.dangerlevel(), 1)
    def test_increment_dangerlevel_repeatedly(self):
        self.testsquare.set_dangerlevel(0)
        self.assertEqual(self.testsquare.dangerlevel(), 0)
        self.testsquare.increment_dangerlevel(5)
        self.assertEqual(self.testsquare.dangerlevel(), 5)
        
    def test_set_mine(self):
        self.assertEqual(self.testsquare.mine(), False)
        self.testsquare.set_mine()
        self.assertEqual(self.testsquare.mine(), True)
    
    def test_parent_grid(self):
        self.assertEqual(self.testsquare.parent_grid(), self.tempgrid)


if __name__ == '__main__':
    unittest.main()