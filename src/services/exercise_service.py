from entities.exercise import Exercise
from entities.user import User

from repositories.exercise_repository import (
    exercise_repository as default_todo_repository
)


class InvalidCredentialsError(Exception):
    pass


class UsernameExistsError(Exception):
    pass


class ExerciseService:
    """Sovelluslogiikasta vastaa luokka."""

    def __init__(
        self,
        exercise_repository = default_exercise_repository,
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            exercise_repository:
                Vapaaehtoinen, oletusarvoltaan default ExerciseRepository-olio.
                Olio, jolla on ExerciseRepository-luokkaa vastaavat metodit.
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._exercise_repository = exercise_repository
        self._user_repository = user_repository

    def create_exercise(self, type, attempts, hint=None, game=None, ex_id=None):
        """Luo uuden tehtävän.

        Args:
            type:
                Merkkijonoarvo, joka kuvaa tehtävää.
            attemptsLeft:
                 Yksityinen.
                 Kokonaislukuarvo, joka kuvaa yritysten määrää.
           hint:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joka on tehtäväkohtainen vihje.
            game:
                Vapaaehtoinen, oletusarvoltaan None.
                Game-olio, joka kuvaa peliä johon tehtävä kuuluu.
            ex_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa tehtävän id:tä.

        Returns:
            Luotu tehtävä Exercise-olion muodossa.
        """

        exercise = Exercise(type=type, attempts=attempts, hint=hint, game=game, ex_id=ex_id)

        return self._exercise_repository.create(exercise)

    def get_undone_todos(self):
        """Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät.

        Returns:
            Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät Exercise-olioden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """

        if not self._user:
            return []

        exercises = self._exercise_repository.find_by_username(self._user.username)
        undone_exercises = filter(lambda exercise: not exercise.done, exercises)

        return list(undone_exercises)

    def set_exercise_done(self, ex_id):
        """Asettaa tehtävän tehdyksi.

        Args:
            todo_id: Merkkijonoarvo, joka kuvaa tehtävän id:tä.
        """

        self._exercise_repository.set_done(ex_id)

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.

        Args:
            username: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa kirjautuvan käyttäjän salasanaa.
        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, kun käyttäjätunnus ja salasana eivät täsmää.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def get_current_user(self):
        """Paluttaa kirjautuunen käyttäjän.

        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        """
        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            User-oliota sisältä lista kaikista käyttäjistä.
        """
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa sen sisään.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            login:
                Vapaahtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.

        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.

        Returns:
            Luotu käyttäjä User-olion muodossa.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user


todo_service = ExerciseService()