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
    """

    def __init__(self, type, user, game_id=None):
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
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko peli ohi.

        """

        self.structure = type[0]
        self.game_type = type[1]
        self.user = user
        self.game_id = game_id or str(uuid.uuid4())
        self.__generator = QuestionGenerator(self.structure, self.game_type, self.user.skill)
        self.__problems = self.__generator.fetch_problems(1)
        self.done = False

    def player(self):
        """ Palauttaa peliä pelaavan User-olion. """
        return self.user

    def problems(self):
        """ Palauttaa Game-olioon liittyvät tehtävät."""
        return self.__problems

    def set_done(self, id):
        self.__problems[id].done = True

    def fetch_problems(self, n):
        self.__problems = self.__generator.fetch_problems(n)