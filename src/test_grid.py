from grid import Grid
from square import Square
import square
import unittest

class Test_Grid(unittest.TestCase):
    def setUp(self):
        self.testgrid = Grid(10, 10, Square)

    def test_all_objects(self):
        tempgrid = Grid(10, 10, Square)
        self.assertEqual(len(tempgrid.all_objects()), 100)
        tempgrid = Grid(2, 2, Square)
        self.assertEqual(len(tempgrid.all_objects()), 4)
    
    def test_all_objects_filtered(self):
        tempgrid = Grid(5, 5, Square)
        self.assertEqual(tempgrid.all_objects_filtered(square.mined), [])
        tempgrid.object_at(1,1).set_mine()
        tempgrid.object_at(3,4).set_mine()
        mined = [tempgrid.object_at(1,1), tempgrid.object_at(3,4)]
        self.assertEqual(tempgrid.all_objects_filtered(square.mined), mined)
        tempgrid.object_at(1,1).reveal()
        tempgrid.object_at(3,4).reveal()
        revealed = [tempgrid.object_at(1,1), tempgrid.object_at(3,4)]
        self.assertEqual(tempgrid.all_objects_filtered(square.revealed), revealed)
        
    def test_neighbors_topleft(self):
        comparison = [self.testgrid.object_at(0,1), self.testgrid.object_at(1,1),
                      self.testgrid.object_at(1,0)]
        for location in comparison:
            self.assertIn(location, self.testgrid.neighbors(0,0))
    def test_neighbors_topright(self):
        comparison = [self.testgrid.object_at(9,1), self.testgrid.object_at(8,0),
                      self.testgrid.object_at(8,1)]
        for location in comparison:
            self.assertIn(location, self.testgrid.neighbors(9,0))
    def test_neighbors_bottomleft(self):
        comparison = [self.testgrid.object_at(0,8), self.testgrid.object_at(1,9),
                      self.testgrid.object_at(1,8)]
        for location in comparison:
            self.assertIn(location, self.testgrid.neighbors(0,9))
    def test_neighbors_bottomright(self):
        comparison = [self.testgrid.object_at(9,8), self.testgrid.object_at(8,9),
                      self.testgrid.object_at(8,8)]
        for location in comparison:
            self.assertIn(location, self.testgrid.neighbors(9,9))
    def test_neighbors_middle(self):
        comparison = [self.testgrid.object_at(3,2), self.testgrid.object_at(3,4),
                      self.testgrid.object_at(2,3), self.testgrid.object_at(4,3),
                      self.testgrid.object_at(2,2), self.testgrid.object_at(4,4),
                      self.testgrid.object_at(2,4), self.testgrid.object_at(4,2)]
        for location in comparison:
            self.assertIn(location, self.testgrid.neighbors(3,3))


if __name__ == '__main__':
    unittest.main()