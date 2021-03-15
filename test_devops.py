import unittest
from devops import suma

class TestDevOps(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(suma(10,5), 15)
        self.assertEqual(suma(-5,5), 0)
        self.assertEqual(suma(-6,-4), -10)

    def test_suma2(self):
        self.assertEqual(suma(-4,5), 1)
        self.assertEqual(suma(2,0), 2)
        self.assertEqual(suma(-8,0), -8)



if __name__ == '__main__':
    unittest.main()
