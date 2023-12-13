from entities.user import User
from entities.game import Game
from repositories.user_repository import user_repository as default_user_repository


class GameService():
    """ Sovelluslogiikassa käyttäjien tietokantojen, yhden peli-instanssin ja sovelluksen välisestä
        kommunikaatiosta vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Attributes:
            game:
                Game-olio, joka kuvaa pelattava peliä.
        """
        self._game = None

    def create_game(self, type, structure, user):
        new_game = Game((type, structure), user)
        self._game = new_game

    def increase_points(self):
        if self._game:
            self._game.user().increase_points()

    def get_exercises(self):
        """ Palauttaa kaikki tehtävät.
        """
        if not self._game.user:
            return []

        return self._game.problems()

    def get_undone_exercises(self):
        """ Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät.

        Returns:
            Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät Exercise-olioden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """

        if not self._game.user:
            return []

        self._game.fetch_problems(1)
        exercises = self._game.problems()
        undone_exercises = filter(
            lambda exercise: not exercise.done, exercises)

        return list(undone_exercises)

    def set_exercise_done(self, ex_id):
        """Asettaa tehtävän tehdyksi.

        Args:
            todo_id: Merkkijonoarvo, joka kuvaa tehtävän id:tä.
        """

        self._game.set_done(ex_id)


    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos.
        """
        self._user = None

game_service = GameService()