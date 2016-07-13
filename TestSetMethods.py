import linearset
import unittest


class TestSetMethods(unittest.TestCase):
    def setUp(self):
        self.testSetA = linearset.Set()
        self.testSetB = linearset.Set()

    def tearDown(self):
        pass

    def test_subset(self):
        self.testSetA.add('a')
        self.testSetB.add('a')
        self.assertEqual(True, self.testSetA.isSubsetOf(self.testSetB))


if __name__ == '__main__':
    unittest.main()
