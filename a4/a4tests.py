import unittest
from a4classes import myVector, myVectorRepository
from a4controller import Controller

class Test(unittest.TestCase):
    def setUp(self):
        empty_list = []
        self.repo = myVectorRepository(empty_list)
        self.vector_controller = Controller(self.repo)

    def tearDown(self):
        self.repo = None

    def test_add_vector(self):
        vector = myVector(1, 'r', 1, [1, 2, 3])
        self.repo.add(vector)
        self.assertEqual(len(self.repo.get_vectors()), 1)
        self.assertEqual(self.repo.get_vectors()[0].getNameId(), 1)
        self.assertEqual(self.repo.get_vectors()[0].getValues(), [1, 2, 3])

    def test_get_all_vectors(self):
        vector1 = myVector(1, 'r', 1, [1, 2])
        vector2 = myVector(2, 'g', 1, [3, 4])
        self.repo.add(vector1)
        self.repo.add(vector2)
        vectors = self.repo.get_vectors()
        self.assertEqual(len(vectors), 2)
        self.assertEqual(vectors[0].getNameId(), 1)
        self.assertEqual(vectors[1].getNameId(), 2)

    def test_get_vector_at_index(self):
        vector = myVector(3, 'b', 1, [1, 2, 3])
        self.repo.add(vector)
        retrieved_vector = self.repo.get_vector_index(0)
        self.assertEqual(retrieved_vector.getNameId(), 3)
        self.assertEqual(retrieved_vector.getColor(), 'b')
        self.assertEqual(retrieved_vector.getValues(), [1, 2, 3])

    def test_update_vector_at_index(self):
        vector = myVector(4, 'y', 1, [5, 6])
        self.repo.add(vector)
        self.repo.update_vector_index(0, 5, 'm', 1, [7, 8])
        updated_vector = self.repo.get_vector_index(0)
        self.assertEqual(updated_vector.getNameId(), 5)
        self.assertEqual(updated_vector.getColor(), 'm')
        self.assertEqual(updated_vector.getValues(), [7, 8])

    def test_delete_vector_by_index(self):
        vector = myVector(6, 'g', 1, [9, 10])
        self.repo.add(vector)
        self.repo.del_index(0)
        self.assertEqual(len(self.repo.get_vectors()), 0)

    def test_delete_vector_by_nameID(self):
        vector1 = myVector(7, 'r', 1, [1])
        vector2 = myVector(8, 'g', 1, [2])
        self.repo.add(vector1)
        self.repo.add(vector2)

        self.repo.del_id(7)

        self.assertEqual(len(self.repo.get_vectors()), 2)
        self.assertEqual(self.repo.get_vectors()[0].getNameId(), 7)

    def test_sum_same_color(self):
        vector1 = myVector(9, 'g', 1, [1, 2])
        vector2 = myVector(10, 'g', 1, [3, 4])
        self.repo.add(vector1)
        self.repo.add(vector2)
        total_sum = self.repo.sum_same_col('g')
        self.assertEqual(total_sum, 10)

    def test_update_vector_color_by_id(self):
        vector = myVector(11, 'y', 1, [5, 6])
        self.repo.add(vector)
        self.repo.update_col_byID(11, 'b')
        updated_vector = self.repo.get_vectors()[0]
        self.assertEqual(updated_vector.getColor(), 'b')

    def test_delete_all_vectors(self):
        vector1 = myVector(12, 'r', 1, [1])
        vector2 = myVector(13, 'g', 1, [2])
        self.repo.add(vector1)
        self.repo.add(vector2)
        self.repo.del_all_vectors()
        self.assertEqual(len(self.repo.get_vectors()), 0)

def runTests():
    # Unittest has a built in option to load all tests. We will store these in x
    x = unittest.TestLoader().loadTestsFromTestCase(Test)

    # We start the test and run it (again with the built in options from unittest)
    runner = unittest.TextTestRunner()
    runner.run(x)

if __name__ == '__main__':
    unittest.main()