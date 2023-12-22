import unittest
from src.services.user_service import UserService
from src.entities.user import User


class MockUserRepo:
    def __init__(self):
        self.users = []
        self.user = User("name", "pw", "easy")

    def find_all(self):
        return self.users

    def find_by_username(self, name):
        for e in self.users:
            if e.username == name:
                return e
        return None

    def create(self, u):
        self.users.append(u)

    def delete_all(self):
        self.users = []


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.test_repo = MockUserRepo()
        self.user_service = UserService(self.test_repo)

    def test_init(self):
        self.assertEqual(self.user_service.get_users(), [])

    def test_login(self):
        self.user_service.create_user("name", "pw")
        self.user_service.login("name", "pw")
        self.assertEqual(self.user_service.get_current_user().username, "name")

    def test_logout(self):
        self.user_service.create_user("name", "pw")
        self.user_service.login("name", "pw")
        self.assertEqual(self.user_service.get_current_user().username, "name")
        self.user_service.logout()
        self.assertEqual(self.user_service.get_current_user(), None)
