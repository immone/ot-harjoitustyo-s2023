import unittest
from src.entities.game import Game
from src.entities.user import User


class TestExercise(unittest.TestCase):

    def setUp(self):
        self.mockUser = User("User", "secretPass", "Beginner")
        self.game = Game("single",
                         5,
                         "easy",
                         self.mockUser,
                         123)

    def test_initial_user(self):
        self.assertEqual(self.game.player(), self.mockUser)
