from entities.game import Game


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

    def get_current_game(self):
        """ Hakee pelattavan Game-olion. """
        return self._game

    def create_game(self, game_type, structure, user):
        """ Luo Game-olion, joka kuvaa pelattavaa peliä ja palauttaa sen. """

        new_game = Game((game_type, structure), user)
        self._game = new_game
        self._game.fetch_problems(10)
        return new_game

    def increase_points(self):
        """ Kasvattaa pelin pisteitä yhdellä. """

        if self._game:
            self._game.correct += 1

    def answered(self):
        """ Hakee vastattujen kysyksien määrän pelattavasta pelistä. """

        return self._game.answered

    def correct(self):
        """ Hakee oikein vastattujen kysyksien määrän pelattavasta pelistä. """

        return self._game.correct

    def get_exercises(self):
        """ Palauttaa kaikki tehtävät. """

        if not self._game.user:
            return []

        return self._game.exercises()

    def get_undone_exercises(self):
        """ Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät.

        Returns:
            Palauttaa kirjautuneen käyttäjän tekemättömät tehtävät Exercise-olioden listana.
            Jos kirjautunutta käyttäjää ei ole, palauttaa tyhjän listan.
        """

        if not self._game.user:
            return []

        exercises = self.get_exercises()
        undone_exercises = filter(
            lambda exercise:  exercise.done is False, exercises)
        print(exercises)
        return list(undone_exercises)

    def set_exercise_done(self, ex_id):
        """Asettaa tehtävän tehdyksi.

        Args:
            todo_id: Merkkijonoarvo, joka kuvaa tehtävän id:tä.
        """
        if self._game:
            self._game.answered += 1
            self._game.set_done(ex_id)


game_service = GameService()
