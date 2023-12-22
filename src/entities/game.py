import uuid
from entities.question_generator import QuestionGenerator


class Game:
    """ Luokka, joka kuvaa yksittäistä harjoituspeliä.

        Attributes:
            type:
                Merkkijono arvoista koostuva pari, jonka ensimmäinen arvo kuvaa
                pelin aihealuetta ja toinen kysymysten laatua
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa tehtävän omistajaa.
            game_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa pelin id:tä.
            generator:
                Viittaus QuestionGenerator-olioon, joka luo peliin tehtäviä.
            structure:
                Kuvaa pelin algebrallista rakennetta.
            game_type:
                Kuvaa pelin tyyppiä, ts. minkälaisia kysymyksiä siinä on.
    """

    def __init__(self, game_type, user, game_id=None):
        """Luokan konstruktori, joka luo uuden tehtävän.

        Args:
            type:
                Merkkijono arvoista koostuva pari, jonka ensimmäinen arvo kuvaa
                pelin aihealuetta ja toinen kysymysten laatua
            user:
                Vapaaehtoinen, oletusarvoltaan None.
                User-olio, joka kuvaa tehtävän omistajaa.
            game_id:
                Vapaaehtoinen, oletusarvoltaan generoitu uuid.
                Merkkijonoarvo, joku kuvaa pelin id:tä.
        """

        self.structure = game_type[1]
        self.game_type = game_type[0]
        self.user = user
        self.answered = 0
        self.correct = 0
        self.game_id = game_id or str(uuid.uuid4())
        self.generator = QuestionGenerator(
            self.game_type, self.user.skill, self.structure)
        self.problems = self.generator.fetch_problems(5)
        self.done = False

    def is_over(self):
        """ Palauttaa tiedo siitä, oko peli ohi. """
        return self.answered == len(self.problems)

    def player(self):
        """ Palauttaa peliä pelaavan User-olion. """
        return self.user

    def exercises(self):
        """ Palauttaa Game-olioon liittyvät tehtävät."""
        return self.problems

    def set_done(self, ex_id):
        """ Asettaa parametrin annetun ID:n omaavan tehtävän tehdyksi. """
        for ex in self.problems:
            if ex.id == ex_id:
                ex.done = True

    def fetch_problems(self, n):
        """ Asettaa attribuutin self.problems arvoksi generoidun listan ongelmia. """
        self.problems = self.generator.fetch_problems(n)
