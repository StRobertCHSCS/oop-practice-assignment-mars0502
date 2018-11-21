import unittest
import Coin as CoinClass

class TestCoin (unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.values = ['heads', 'tails']
        cls.coin = CoinClass.Coin()

    def test_instance_creation(self):
        self.assertIsInstance(self.coin, CoinClass.Coin, "The object is an instance of coin")

    def test_default_value(self):
        self.assertIn(self.coin.face, self.values)

    def test_get_face(self):
        self.assertIn(self.coin.get_face(), self.values)

    def test_flip(self):
        self.coin.flip()
        self.assertIn(self.coin.get_face(), self.values)


if __name__ == '__main__':
    unittest.main()
