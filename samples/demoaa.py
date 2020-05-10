import unittest

class testa(unittest.TestCase):

    @unittest.skipIf(True,'dd')
    def test_add(self):
        print('test_add')
        self.assertEqual(1+1,2)

if __name__ == '__main__':
    unittest.main()