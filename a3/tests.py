import unittest
from classes import PointRepository, Point

testList = []

class Test(unittest.TestCase):
    # We start the repository
    def setUp(self):
        self.repo = PointRepository(testList)

    # We clean up the repository by calling tearDown
    def tearDown(self):
        self.repo = None

    # 1. addPoint
    def test_addPoint(self):
        self.repo.addPoint(Point(5, 5, "green"))

        self.assertEqual(self.repo.getPoints()[-1].getColor(), "green")
        self.assertEqual(self.repo.getPoints()[-1].getX(), 5)
        self.assertEqual(self.repo.getPoints()[-1].getY(), 5)

    # 2. getPoints
    def test_getPoints(self):
        points = self.repo.getPoints()

        self.assertEqual(points[0].getColor(), "red")
        self.assertEqual(points[1].getColor(), "blue")
        self.assertEqual(len(points), 2)

    # 3. getPointAtIndex
    def test_getPointAtIndex(self):
        self.assertEqual(self.repo.getPointAtIndex(0).getColor(), "red")
        self.assertEqual(self.repo.getPointAtIndex(1).getX(), 3)
        self.assertEqual(self.repo.getPointAtIndex(1).getY(), 4)

    # 4. getPointsOfColor
    def test_getPointsOfColor(self):
        red_points = self.repo.getPointsOfColor("red")

        self.assertEqual(len(red_points), 1)
        self.assertEqual(red_points[0].getX(), 1)
        self.assertEqual(red_points[0].getY(), 2)

    # 5. getPointsInsideSquare
    def test_getPointsInsideSquare(self):
        square_points = self.repo.getPointsInsideSquare(Point(0, 0, 'magenta'), 5)

        self.assertEqual(len(square_points), 1)
        self.assertEqual(square_points[0].getX(), 1)
        self.assertEqual(square_points[0].getY(), 2)

    # 6. getMinDistance
    def test_getMinDistance(self):
        min_distance = self.repo.getMinDistance()

        self.assertGreater(min_distance, 0)
        self.assertIsInstance(min_distance, float)
        self.assertEqual(min_distance, 4)

    # 7. updateByIndex
    def test_updateByIndex(self):
        self.repo.updateByIndex(0, 5, 5, "green")

        self.assertEqual(self.repo.getPointAtIndex(0).getX(), 5)
        self.assertEqual(self.repo.getPointAtIndex(0).getY(), 5)
        self.assertEqual(self.repo.getPointAtIndex(0).getColor(), "green")

    # 8. deleteByIndex
    def test_deleteByIndex(self):
        self.repo.deleteByIndex(1)
        self.assertEqual(len(self.repo.getPoints()), 1)
        self.assertEqual(self.repo.getPoints()[0].getColor(), "red")


    # 9. delPointsInsideSquare
    def test_delPointsInsideSquare(self):
        self.repo.addPoint(Point(0, 0, "blue"))
        self.repo.delPointsInsideSquare(Point(0, 0, 'magenta'), 5)
        self.assertEqual(len(self.repo.getPoints()), 1)
        self.assertEqual(self.repo.getPoints()[0].getColor(), "red")

    # 10. plotAllPoints doesn't require testing

    # 11. getMaxDistance
    def test_getMaxDistance(self):
        max_distance = self.repo.getMaxDistance()

        self.assertGreater(max_distance, 0)
        self.assertIsInstance(max_distance, float)
        self.assertEqual(max_distance, 4)

    # 12. shiftPointsOnX
    def test_shiftPointsOnX(self):
        self.repo.shiftPointsOnX()
        self.assertTrue(all(pt.getY() == 0 for pt in self.repo.getPoints()))
        self.assertEqual(self.repo.getPoints()[0].getX(), 1)

    # 13. delPtsInsideCircle
    def test_delPtsInsideCircle(self):
        self.repo.delPtsInsideCircle(Point(0, 0, 'magenta'), 6)
        self.assertEqual(len(self.repo.getPoints()), 0)
        self.repo.addPoint(Point(10, 10, "blue"))
        self.repo.delPtsInsideCircle(Point(5, 5, 'magenta'), 3)
        self.assertEqual(len(self.repo.getPoints()), 1)
        self.assertEqual(self.repo.getPoints()[0].getColor(), "blue")

def runTests():
    # Unittest has a built in option to load all tests. We will store these in x
    x = unittest.TestLoader().loadTestsFromTestCase(Test)

    # We start the test and run it (again with the built in options from unittest)
    runner = unittest.TextTestRunner()
    runner.run(x)

if __name__ == "__main__":
    unittest.main()

