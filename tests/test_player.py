import unittest
from pygame_goku_in_python.player import Player


class TestPlayer(unittest.TestCase):

    def test_init(self):
        player = Player()
        self.assertIsInstance(player, Player)
        self.assertEqual(player.life, 100)
        self.assertEqual(player.x, 0)
        self.assertEqual(player.y, 0)


if __name__ == '__main__':
    unittest.main()
