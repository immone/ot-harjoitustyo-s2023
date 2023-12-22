import unittest
from src.entities.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.mockUser = User("User", "secretPass", "easy")

    def test_initialization_all_games(self):
        self.assertEqual(self.mockUser.all_games, [])

    def test_initialization_name(self):
        self.assertEqual(self.mockUser.username, "User")

    def test_initialization_password(self):
        self.assertEqual(self.mockUser.password, "secretPass")

    def test_initialization_skill(self):
        self.assertEqual(self.mockUser.skill, "easy")

    def test_update_skill(self):
        self.mockUser.update_skill("hard")
        self.assertEqual(self.mockUser.skill, "hard")
